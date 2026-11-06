from pyscript import document
#making a dictionary conataining elements information

elements= {'H': ('Hydrogen', 1, 1.008),
            'He' :('Helium', 2, 4.0026),
            'C': ('Carbon', 6, 12.011),
            'N': ('Nitrogen', 7, 14.007),
            'O': ('Oxygen', 8, 15.998),
            'F': ('Flourine', 9, 18.998),
            'Ne': ('Neon', 10, 20.180),
            'P': ('Phosphorus', 15, 30.974),
            'S': ('Sulfur', 16, 32.066),
            'Cl': ('Chlorine', 17, 35.453),
            'Ar': ('Argon', 18, 39.948),
            'Se': ('Selenium', 34, 78.972),
            'Br': ('Bromine', 35, 79.904),
            'Kr': ('Krypton', 36, 84.80),
            'I': ('Iodine', 53, 126.904),
            'Xe': ('Xenon', 54, 131.29),
            'At': ('Astanine', 85, 209.987),
            'Rn': ('Radon', 86, 222.018),
            'Ts': ('Tennessine', 117, 294),
            'Og': ('Oganesson', 118, 294),
}
#element name : element, atomic #, atomic mass
#key : value
#element name, 

#function to search for an element
def search_element(e):
    #get the input from the html. 
    Element1 = document.getElementById("element1").value

    #retrieve info from the dictionary 
    result = elements.get(Element1, ("Oops! This element is not a non-metal...", 0, 0))

    Element0 = Element1.capitalize()

    #display the result in html
    #symbol, name, atomic#, atomic mass
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]