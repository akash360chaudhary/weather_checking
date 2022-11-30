from tkinter import *
from tkinter import ttk
import requests as rs


def data_get():
    city = city_name.get()
    data = rs.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    wc_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=(data["main"]["temp"]-273.15))
    wp_label1.config(text=data["main"]["pressure"])


root = Tk()
root.geometry("500x500")
root.minsize(500, 500)
root.maxsize(500, 500)
root.title("Weather Checking")
root.config(bg="lightgrey")

# App Name
name_label = Label(root, text="Live Weather Checking", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=40, height=50, width=450)

# State Box
city_name = StringVar()
state_names = ["Adilabad",	"Agar Malwa",	"Agra",	"Ahmedabad",	"Ahmednagar",	"Aizawl",	"Ajmer",	"Akola",	"Alappuzha",	"Aligarh",	"Alipurduar",	"Alirajpur",	"Almora",	"Alwar",	"Ambala",	"Ambedkar Nagar",	"Amethi",	"Amravati",	"Amreli",	"Amritsar",	"Amroha",	"Anand",	"Anantapur",	"Anantnag",	"Angul",	"Anjaw",	"Anuppur",	"Araria",	"Aravalli",	"Ariyalur",	"Arwal",	"Ashoknagar",	"Auraiya",	"Aurangabad",	"Aurangabad",	"Ayodhya",	"Azamgarh",	"Bagalkot",	"Bageshwar",	"Baghpat",	"Bahraich",	"Bajali",	"Baksa",	"Balaghat",	"Balangir",	"Balasore",	"Ballia",	"Balod",	"Baloda Bazar",	"Balrampur",	"Balrampur",	"Banaskantha",	"Banda",	"Bandipora",	"Bangalore Rural",	"Bangalore Urban",	"Banka",	"Bankura",	"Banswara",	"Barabanki",	"Baramulla",	"Baran",	"Bareilly",	"Bargarh",	"Barmer",	"Barnala",	"Barpeta",	"Barwani",	"Bastar",	"Basti",	"Bathinda",	"Beed",	"Begusarai",	"Belgaum",	"Bellary",	"Bemetara",	"Betul",	"Bhadohi",	"Bhadradri Kothagudem",	"Bhadrak",	"Bhagalpur",	"Bhandara",	"Bharatpur",	"Bharuch",	"Bhavnagar",	"Bhilwara",	"Bhind",	"Bhiwani",	"Bhojpur",	"Bhopal",	"Bidar",	"Bijapur",	"Bijnor",	"Bikaner",	"Bilaspur",	"Bilaspur",	"Birbhum",	"Bishnupur",	"Biswanath",	"Bokaro",	"Bongaigaon",	"Botad",	"Boudh",	"Budaun",	"Budgam",	"Bulandshahr",	"Buldhana",	"Bundi",	"Burhanpur",	"Buxar",	"Cachar",	"Central Delhi",	"Central Siang",	"Chachaura",	"Chamarajanagar",	"Chamba",	"Chamoli",	"Champawat",	"Champhai",	"Chandauli",	"Chandel",	"Chandigarh",	"Chandrapur",	"Changlang",	"Charaideo",	"Charkhi Dadri",	"Chatra",	"Chengalpattu",	"Chennai",	"Chhatarpur",	"Chhindwara",	"Chhota Udaipur",	"Chikkaballapur",	"Chikkamagaluru",	"Chirang",	"Chitradurga",	"Chitrakoot",	"Chittoor",	"Chittorgarh",	"Churachandpur",	"Churu",	"Coimbatore",	"Cooch Behar",	"Cuddalore",	"Cuttack",	"Dadra Nagar Haveli",	"Dahod",	"Dakshin Dinajpur",	"Dakshina Kannada",	"Daman",	"Damoh",	"Dang",	"Dantewada",	"Darbhanga",	"Darjeeling",	"Darrang",	"Datia",	"Dausa",	"Davanagere",	"Debagarh",	"Dehradun",	"Deoghar",	"Deoria",	"Devbhoomi Dwarka",	"Dewas",	"Dhalai",	"Dhamtari",	"Dhanbad",	"Dhar",	"Dharmapuri",	"Dharwad",	"Dhemaji",	"Dhenkanal",	"Dholpur",	"Dhubri",	"Dhule",	"Dibang Valley",	"Dibrugarh",	"Dima Hasao",	"Dimapur",	"Dindigul",	"Dindori",	"Diu",	"Doda",	"Dumka",	"Dungarpur",	"Durg",	"East Champaran",	"East Delhi",	"East Garo Hills",	"East Godavari",	"East Jaintia Hills",	"East Kameng",	"East Khasi Hills",	"East Siang",	"East Sikkim",	"East Singhbhum",	"Ernakulam",	"Erode",	"Etah",	"Etawah",	"Faridabad",	"Faridkot",	"Farrukhabad",	"Fatehabad",	"Fatehgarh Sahib",	"Fatehpur",	"Fazilka",	"Firozabad",	"Firozpur",	"Gadag",	"Gadchiroli",	"Gajapati",	"Ganderbal",	"Gandhinagar",	"Ganjam",	"Garhwa",	"Gariaband",	"Gaurela Pendra Marwahi",	"Gautam Buddha Nagar",	"Gaya",	"Ghaziabad",	"Ghazipur",	"Gir Somnath",	"Giridih",	"Goalpara",	"Godda",	"Golaghat",	"Gomati",	"Gonda",	"Gondia",	"Gopalganj",	"Gorakhpur",	"Gulbarga",	"Gumla",	"Guna",	"Guntur",	"Gurdaspur",	"Gurugram",	"Gwalior",	"Hailakandi",	"Hamirpur",	"Hamirpur",	"Hanumangarh",	"Hapur",	"Harda",	"Hardoi",	"Haridwar",	"Hassan",	"Hathras",	"Haveri",	"Hazaribagh",	"Hingoli",	"Hisar",	"Hnahthial",	"Hojai",	"Hooghly",	"Hoshangabad",	"Hoshiarpur",	"Howrah",	"Hyderabad",	"Idukki",	"Imphal East",	"Imphal West",	"Indore",	"Jabalpur",	"Jagatsinghpur",	"Jagtial",	"Jaipur",	"Jaisalmer",	"Jajpur",	"Jalandhar",	"Jalaun",	"Jalgaon",	"Jalna",	"Jalore",	"Jalpaiguri",	"Jammu",	"Jamnagar",	"Jamtara",	"Jamui",	"Jangaon",	"Janjgir Champa",	"Jashpur",	"Jaunpur",	"Jayashankar",	"Jehanabad",	"Jhabua",	"Jhajjar",	"Jhalawar",	"Jhansi",	"Jhargram",	"Jharsuguda",	"Jhunjhunu",	"Jind",	"Jiribam",	"Jodhpur",	"Jogulamba",	"Jorhat",	"Junagadh",	"Kabirdham",	"Kadapa",	"Kaimur",	"Kaithal",	"Kakching",	"Kalahandi",	"Kalimpong",	"Kallakurichi",	"Kamareddy",	"Kamjong",	"Kamle",	"Kamrup",	"Kamrup Metropolitan",	"Kanchipuram",	"Kandhamal",	"Kangpokpi",	"Kangra",	"Kanker",	"Kannauj",	"Kannur",	"Kanpur Dehat",	"Kanpur Nagar",	"Kanyakumari",	"Kapurthala",	"Karaikal",	"Karauli",	"Karbi Anglong",	"Kargil",	"Karimganj",	"Karimnagar",	"Karnal",	"Karur",	"Kasaragod",	"Kasganj",	"Kathua",	"Katihar",	"Katni",	"Kaushambi",	"Kendrapara",	"Kendujhar",	"Khagaria",	"Khammam",	"Khandwa",	"Khargone",	"Khawzawl",	"Kheda",	"Kheri",	"Khordha",	"Khowai",	"Khunti",	"Kinnaur",	"Kiphire",	"Kishanganj",	"Kishtwar",	"Kodagu",	"Koderma",	"Kohima",	"Kokrajhar",	"Kolar",	"Kolasib",	"Kolhapur",	"Kolkata",	"Kollam",	"Komaram Bheem",	"Kondagaon",	"Koppal",	"Koraput",	"Korba",	"Koriya",	"Kota",	"Kottayam",	"Kozhikode",	"Kra Daadi",	"Krishna",	"Krishnagiri",	"Kulgam",	"Kullu",	"Kupwara",	"Kurnool",	"Kurukshetra",	"Kurung Kumey",	"Kushinagar",	"Kutch",	"Lahaul Spiti",	"Lakhimpur",	"Lakhisarai",	"Lakshadweep",	"Lalitpur",	"Latehar",	"Latur",	"Lawngtlai",	"Leh",	"Lepa Rada",	"Lohardaga",	"Lohit",	"Longding",	"Longleng",	"Lower Dibang Valley",	"Lower Siang",	"Lower Subansiri",	"Lucknow",	"Ludhiana",	"Lunglei",	"Madhepura",	"Madhubani",	"Madurai",	"Mahabubabad",	"Maharajganj",	"Mahasamund",	"Mahbubnagar",	"Mahe",	"Mahendragarh",	"Mahisagar",	"Mahoba",	"Maihar",	"Mainpuri",	"Majuli",	"Malappuram",	"Malda",	"Malkangiri",	"Mamit",	"Mancherial",	"Mandi",	"Mandla",	"Mandsaur",	"Mandya",	"Mansa",	"Mathura",	"Mau",	"Mayiladuthurai",	"Mayurbhanj",	"Medak",	"Medchal",	"Meerut",	"Mehsana",	"Mewat",	"Mirzapur",	"Moga",	"Mohali",	"Mokokchung",	"Mon",	"Moradabad",	"Morbi",	"Morena",	"Morigaon",	"Muktsar",	"Mulugu",	"Mumbai City",	"Mumbai Suburban",	"Mungeli",	"Munger",	"Murshidabad",	"Muzaffarnagar",	"Muzaffarpur",	"Mysore",	"Nabarangpur",	"Nadia",	"Nagaon",	"Nagapattinam",	"Nagarkurnool",	"Nagaur",	"Nagda",	"Nagpur",	"Nainital",	"Nalanda",	"Nalbari",	"Nalgonda",	"Namakkal",	"Namsai",	"Nanded",	"Nandurbar",	"Narayanpet",	"Narayanpur",	"Narmada",	"Narsinghpur",	"Nashik",	"Navsari",	"Nawada",	"Nayagarh",	"Neemuch",	"Nellore",	"New Delhi",	"Nicobar",	"Nilgiris",	"Nirmal",	"Niwari",	"Nizamabad",	"Noklak",	"Noney",	"North 24 Parganas",	"North Delhi",	"North East Delhi",	"North Garo Hills",	"North Goa",	"North Middle Andaman",	"North Sikkim",	"North Tripura",	"North West Delhi",	"Nuapada",	"Osmanabad",	"Pakke Kessang",	"Pakur",	"Palakkad",	"Palamu",	"Palghar",	"Pali",	"Palwal",	"Panchkula",	"Panchmahal",	"Panipat",	"Panna",	"Papum Pare",	"Parbhani",	"Paschim Bardhaman",	"Paschim Medinipur",	"Patan",	"Pathanamthitta",	"Pathankot",	"Patiala",	"Patna",	"Pauri",	"Peddapalli",	"Perambalur",	"Peren",	"Phek",	"Pherzawl",	"Pilibhit",	"Pithoragarh",	"Poonch",	"Porbandar",	"Prakasam",	"Pratapgarh",	"Pratapgarh",	"Prayagraj",	"Puducherry",	"Pudukkottai",	"Pulwama",	"Pune",	"Purba Bardhaman",	"Purba Medinipur",	"Puri",	"Purnia",	"Purulia",	"Raebareli",	"Raichur",	"Raigad",	"Raigarh",	"Raipur",	"Raisen",	"Rajanna Sircilla",	"Rajgarh",	"Rajkot",	"Rajnandgaon",	"Rajouri",	"Rajsamand",	"Ramanagara",	"Ramanathapuram",	"Ramban",	"Ramgarh",	"Rampur",	"Ranchi",	"Ranga Reddy",	"Ranipet",	"Ratlam",	"Ratnagiri",	"Rayagada",	"Reasi",	"Rewa",	"Rewari",	"Ri Bhoi",	"Rohtak",	"Rohtas",	"Rudraprayag",	"Rupnagar",	"Sabarkantha",	"Sagar",	"Saharanpur",	"Saharsa",	"Sahebganj",	"Saiha",	"Saitual",	"Salem",	"Samastipur",	"Samba",	"Sambalpur",	"Sambhal",	"Sangareddy",	"Sangli",	"Sangrur",	"Sant Kabir Nagar",	"Saran",	"Satara",	"Satna",	"Sawai Madhopur",	"Sehore",	"Senapati",	"Seoni",	"Sepahijala",	"Seraikela Kharsawan",	"Serchhip",	"Shahdara",	"Shahdol",	"Shaheed Bhagat Singh Nagar",	"Shahjahanpur",	"Shajapur",	"Shamli",	"Sheikhpura",	"Sheohar",	"Sheopur",	"Shi Yomi",	"Shimla",	"Shimoga",	"Shivpuri",	"Shopian",	"Shravasti",	"Siddharthnagar",	"Siddipet",	"Sidhi",	"Sikar",	"Simdega",	"Sindhudurg",	"Singrauli",	"Sirmaur",	"Sirohi",	"Sirsa",	"Sitamarhi",	"Sitapur",	"Sivaganga",	"Sivasagar",	"Siwan",	"Solan",	"Solapur",	"Sonbhadra",	"Sonipat",	"Sonitpur",	"South 24 Parganas",	"South Andaman",	"South Delhi",	"South East Delhi",	"South Garo Hills",	"South Goa",	"South Salmara-Mankachar",	"South Sikkim",	"South Tripura",	"South West Delhi",	"South West Garo Hills",	"South West Khasi Hills",	"Sri Ganganagar",	"Srikakulam",	"Srinagar",	"Subarnapur",	"Sukma",	"Sultanpur",	"Sundergarh",	"Supaul",	"Surajpur",	"Surat",	"Surendranagar",	"Surguja",	"Suryapet",	"Tamenglong",	"Tapi",	"Tarn Taran",	"Tawang",	"Tehri",	"Tengnoupal",	"Tenkasi",	"Thane",	"Thanjavur",	"Theni",	"Thiruvananthapuram",	"Thoothukudi",	"Thoubal",	"Thrissur",	"Tikamgarh",	"Tinsukia",	"Tirap",	"Tiruchirappalli",	"Tirunelveli",	"Tirupattur",	"Tiruppur",	"Tiruvallur",	"Tiruvannamalai",	"Tiruvarur",	"Tonk",	"Tuensang",	"Tumkur",	"Udaipur",	"Udalguri",	"Udham Singh Nagar",	"Udhampur",	"Udupi",	"Ujjain",	"Ukhrul",	"Umaria",	"Una",	"Unakoti",	"Unnao",	"Upper Siang",	"Upper Subansiri",	"Uttar Dinajpur",	"Uttara Kannada",	"Uttarkashi",	"Vadodara",	"Vaishali",	"Valsad",	"Varanasi",	"Vellore",	"Vidisha",	"Vijayanagara",	"Vijayapura",	"Vikarabad",	"Viluppuram",	"Virudhunagar",	"Visakhapatnam",	"Vizianagaram",	"Wanaparthy",	"Warangal Rural",	"Warangal Urban",	"Wardha",	"Washim",	"Wayanad",	"West Champaran",	"West Delhi",	"West Garo Hills",	"West Godavari",	"West Jaintia Hills",	"West Kameng",	"West Karbi Anglong",	"West Khasi Hills",	"West Siang",	"West Sikkim",	"West Singhbhum",	"West Tripura",	"Wokha",	"Yadadri Bhuvanagiri",	"Yadgir",	"Yamunanagar",	"Yanam",	"Yavatmal",	"Zunheboto"]

state = ttk.Combobox(root, values=state_names, font=("Time New Roman", 20, "bold"), textvariable=city_name)
state.place(x=50, y=110, height=40, width=400)

# Search Button
search_button = Button(root, text="Search", font=("Time New Roman", 18, "bold"), command=data_get)
search_button.place(x=200, y=170, height=40, width=100)

# Values Button
# wc -> Weather Climate, wd -> Weather Description, wt -> Weather Temperature, wp -> Weather Pressure
wc_label = Label(root, text="Weather Climate", font=("Time New Roman", 15, "bold"))
wc_label.place(x=20, y=250, height=40, width=220)

wc_label1 = Label(root, text="", font=("Time New Roman", 15, "bold"))
wc_label1.place(x=260, y=250, height=40, width=220)

wd_label = Label(root, text="Weather Description", font=("Time New Roman", 15, "bold"))
wd_label.place(x=20, y=310, height=40, width=220)

wd_label1 = Label(root, text="", font=("Time New Roman", 15, "bold"))
wd_label1.place(x=260, y=310, height=40, width=220)

wt_label = Label(root, text="Weather Temperature", font=("Time New Roman", 15, "bold"))
wt_label.place(x=20, y=370, height=40, width=220)

wt_label1 = Label(root, text="", font=("Time New Roman", 15, "bold"))
wt_label1.place(x=260, y=370, height=40, width=220)

wp_label = Label(root, text="Weather Pressure", font=("Time New Roman", 15, "bold"))
wp_label.place(x=20, y=430, height=40, width=220)

wp_label1 = Label(root, text="", font=("Time New Roman", 15, "bold"))
wp_label1.place(x=260, y=430, height=40, width=220)

root.mainloop()
