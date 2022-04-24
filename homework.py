from bs4 import BeautifulSoup
from urllib import request
import json
import csv
import os


# nuorodos generavimas
class Link:
    def __init__(self, depart, arrival, dep_time, arr_time):
        self.depart = depart
        self.arrival = arrival
        self.dep_time = dep_time
        self.arr_time = arr_time

    def url_creation(self):
        url = f"http://homeworktask.infare.lt/search.php?from={self.depart}&to={self.arrival}&depart={self.dep_time}" \
              f"&return={self.arr_time}"
        return url


# menu, csv trinimas
def input_data():
    while True:
        try:
            input1 = input("Delete old csv file? 'CAPS' (Y/N):")
            if input1 == "Y":
                os.remove("flights.csv")
                print("Csv deleted")
                continue
            elif input1 == "N":
                input_from = input("From (MAD, JFK, CPH):")
                input_to = input("To (AUH, FUE, MAD):")
                input_date_dep = input("Depart time (mmmm-mm-dd):")
                input_date_arr = input("Return time (mmmm-mm-dd):")
                input_specific = input("Do you want specific connection airport? (Y/N)")
                if input_specific == "Y":
                    input_specific_airp = input("Input specific connection airport: (TFN, LPA, ...)")
                    input_direct = None
                elif input_specific == "N":
                    input_direct = input("Do you want only direct flights? (Y/N)")
                    input_specific_airp = None
                else:
                    input_specific_airp = None
                    input_direct = None
            else:
                print("Error, try again.")
                continue
            return input_from, input_to, input_date_dep, input_date_arr, input_specific_airp, input_direct
        except FileNotFoundError:
            print("No file to delete.")


input_from, input_to, input_date_dep, input_date_arr, input_specific_airp, input_direct = input_data()
flight = Link(input_from, input_to, input_date_dep, input_date_arr)
url = flight.url_creation()


# json uzkrovimas
def load_json_data():
    var_n = 1
    while var_n == 1:
        try:
            html = request.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            site_jsn = json.loads(soup.text)
            var_n += 1
            return site_jsn
        except ValueError:
            print("Failed to find flights, exiting.")
            exit()

site_jsn = load_json_data()


def extraction():

# kintamieji
    var_x = 1
    var_y = 0
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    num_of_ItemsInList_if_flight_direct = 14

# listai
    list1 = []
    list_out = []
    list_inb = []
    list_final = []
    list_final_spec_airp = []
    list_final_direct_flights = []
    list_recomm_id = []
    list_final2 = []


# rekomendaciju listo sudarymas
    while True:
        try:
            identity = site_jsn["body"]["data"]["journeys"][var1]["recommendationId"]
            var1 += var_x
            list1.append(identity)
        except IndexError:
            break


# istraukimas info is JSON
    while list1:
        try:
            list_of_connections = []
            connections = site_jsn["body"]["data"]["journeys"][var2]["flights"]
            for n in connections:
                list_of_connections.append(n)
            if len(list_of_connections) >= 3:
                var2 += var_x
                continue


            recomm_id = site_jsn["body"]["data"]["journeys"][var2]["recommendationId"]
            if recomm_id == site_jsn["body"]["data"]["totalAvailabilities"][var4]["recommendationId"]:
                tax_var_x = list1.count(recomm_id) - var_x
                price = site_jsn["body"]["data"]["totalAvailabilities"][var4]["total"]
                direction = site_jsn["body"]["data"]["journeys"][var2]["direction"]
                tax1 = site_jsn["body"]["data"]["journeys"][var3]["importTaxAdl"]
                tax2 = site_jsn["body"]["data"]["journeys"][var3 + tax_var_x]["importTaxAdl"]
                tax_total = round((tax1 + tax2), 2)
                dep1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["airportDeparture"]["code"]
                arr1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["airportArrival"]["code"]
                t_dep1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["dateDeparture"].replace("/", "-")
                t_arr1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["dateArrival"].replace("/", "-")
                flight_nr1_code = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["companyCode"]
                flight_nr1_nr = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["number"]
                flight_nr1_full = flight_nr1_code + flight_nr1_nr
                if 3 > len(site_jsn["body"]["data"]["journeys"][var2]["flights"]) >= 2:
                    dep2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["airportDeparture"]["code"]
                    arr2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["airportArrival"]["code"]
                    t_dep2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["dateDeparture"].replace("/",
                                                                                                                   "-")
                    t_arr2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["dateArrival"].replace("/",
                                                                                                                 "-")
                    flight_nr2_code = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["companyCode"]
                    flight_nr2_nr = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["number"]
                    flight_nr2_full = flight_nr2_code + flight_nr2_nr
                    if direction == 'I':
                        full_recom_info = (
                            recomm_id, price, tax_total, dep1, arr1, t_dep1, t_arr1, flight_nr1_full, dep2, arr2,
                            t_dep2, t_arr2, flight_nr2_full
                        )
                        list_out.append(full_recom_info)
                        var2 += var_x
                    elif direction == 'V':
                        full_recom_info = (
                            recomm_id, dep1, arr1, t_dep1, t_arr1, flight_nr1_full, dep2, arr2, t_dep2, t_arr2,
                            flight_nr2_full
                        )
                        list_inb.append(full_recom_info)
                        var2 += var_x
                        var6 += var_x
                elif len(site_jsn["body"]["data"]["journeys"][var2]["flights"]) < 2:
                    if direction == 'I':
                        full_recom_info = (recomm_id, price, tax_total, dep1, arr1, t_dep1, t_arr1, flight_nr1_full)
                        list_out.append(full_recom_info)
                        var2 += var_x
                    elif direction == 'V':
                        full_recom_info = (recomm_id, dep1, arr1, t_dep1, t_arr1, flight_nr1_full)
                        list_inb.append(full_recom_info)
                        var2 += var_x
                        var6 += var_x

            elif recomm_id != site_jsn["body"]["data"]["totalAvailabilities"][var4]["recommendationId"]:
                var4 += var_x
                tax_var_x = list1.count(recomm_id) - var_x
                var3 += list1.count(recomm_id)
                price = site_jsn["body"]["data"]["totalAvailabilities"][var4]["total"]
                direction = site_jsn["body"]["data"]["journeys"][var2]["direction"]
                tax1 = site_jsn["body"]["data"]["journeys"][var3]["importTaxAdl"]
                tax2 = site_jsn["body"]["data"]["journeys"][var3 + tax_var_x]["importTaxAdl"]
                tax_total = round((tax1 + tax2), 2)
                dep1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["airportDeparture"]["code"]
                arr1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["airportArrival"]["code"]
                t_dep1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["dateDeparture"].replace("/", "-")
                t_arr1 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["dateArrival"].replace("/", "-")
                flight_nr1_code = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["companyCode"]
                flight_nr1_nr = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_y]["number"]
                flight_nr1_full = flight_nr1_code + flight_nr1_nr
                if 3 > len(site_jsn["body"]["data"]["journeys"][var2]["flights"]) >= 2:
                    dep2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["airportDeparture"]["code"]
                    arr2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["airportArrival"]["code"]
                    t_dep2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["dateDeparture"].replace("/",
                                                                                                                   "-")
                    t_arr2 = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["dateArrival"].replace("/",
                                                                                                                 "-")
                    flight_nr2_code = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["companyCode"]
                    flight_nr2_nr = site_jsn["body"]["data"]["journeys"][var2]["flights"][var_x]["number"]
                    flight_nr2_full = flight_nr2_code + flight_nr2_nr
                    if direction == 'I':
                        full_recom_info = (
                            recomm_id, price, tax_total, dep1, arr1, t_dep1, t_arr1, flight_nr1_full, dep2, arr2,
                            t_dep2, t_arr2, flight_nr2_full
                        )
                        list_out.append(full_recom_info)
                        var2 += var_x
                    elif direction == 'V':
                        full_recom_info = (
                            recomm_id, dep1, arr1, t_dep1, t_arr1, flight_nr1_full, dep2, arr2, t_dep2, t_arr2,
                            flight_nr2_full
                        )
                        list_inb.append(full_recom_info)
                        var2 += var_x
                elif len(site_jsn["body"]["data"]["journeys"][var2]["flights"]) < 2:
                    if direction == 'I':
                        full_recom_info = (recomm_id, price, tax_total, dep1, arr1, t_dep1, t_arr1, flight_nr1_full)
                        list_out.append(full_recom_info)
                        var2 += var_x
                    elif direction == 'V':
                        full_recom_info = (recomm_id, dep1, arr1, t_dep1, t_arr1, flight_nr1_full)
                        list_inb.append(full_recom_info)
                        var2 += var_x
        except IndexError:
            break


# galutinio skrydziu listo sukurimas
    for i in list_out:
        while True:
            try:
                if i[var_y] == list_inb[var5][var_y]:
                    list_final.append(i + list_inb[var5])
                    list_recomm_id.append(i[var_y])
                    var5 += var_x
                if i[var_y] != list_inb[var5][var_y]:
                    var5 += var_x
                    continue
            except IndexError:
                var5 = var_y
                break
    print("\nFlight data extracted...")


# skrydziu Nr trinimas is duomenu
    for l in list_final:
        list_l = list(l)
        if list_recomm_id[var7] in list_l:
            list_l.remove(list_recomm_id[var7])
            var7 += var_x
            list_final2.append(list_l)


# specifinio oro uosto ieskojimas
    if input_specific_airp != None:
        for n in list_final2:
            if input_specific_airp in n:
                print("found specific airp")
                list_final_spec_airp.append(n)
            else:
                continue


# tik tiesioginiu skrydziu ieskojimas
    if input_direct == "Y":
        for n in list_final2:
            if len(n) <= num_of_ItemsInList_if_flight_direct:
                list_final_direct_flights.append(n)
                print("found direct")
            else:
                continue

    return list_final2, list_final_spec_airp, list_final_direct_flights


# duomenu irasymas i csv
def writing_data():
    list_of_flights, list_final_spec_airp, list_final_direct_flights = extraction()
    if input_specific_airp == None and input_direct == "N":
        with open("flights.csv", "a", encoding="UTF-8", newline="") as file:
            csv_writer = csv.writer(file)
            text_info = "Price, Taxes, Departure, Arrival,Departure time, Arrival time,Flight Nr. etc."
            csv_writer.writerow([text_info])
            for i in list_of_flights:
                csv_writer.writerow(i)
        print("Flight data written, open 'flights.csv'")
    elif input_specific_airp != None:
        with open("flights.csv", "a", encoding="UTF-8", newline="") as file:
            csv_writer = csv.writer(file)
            text_info = "Price, Taxes, Departure, Arrival,Departure time, Arrival time,Flight Nr. etc."
            csv_writer.writerow([text_info])
            for i in list_final_spec_airp:
                csv_writer.writerow(i)
        print(f"Flight data with airport {input_specific_airp} written, open 'flights.csv'")
    elif input_direct == "Y":
        if list_final_direct_flights == []:
            print("Direct flights not found, exiting")
            exit()
        else:
            with open("flights.csv", "a", encoding="UTF-8", newline="") as file:
                csv_writer = csv.writer(file)
                text_info = "Price, Taxes, Departure, Arrival,Departure time, Arrival time,Flight Nr. etc."
                csv_writer.writerow([text_info])
                for i in list_final_direct_flights:
                    csv_writer.writerow(i)
            print(f"Flight data with only direct flights written, open 'flights.csv'")


# paleidimas
writing_data()
