from pyscript import document, display

def checkNum(e):

    num_bers= ["4", "22", "46", "79", "85"]

    num1= document.getElementById("num1").value
    name= "Angelo"

    confirm_num = num1 in num_bers

    message = (f'Sorry {name}, your number is not found.' , f'Yay! {name}, your number is found.')

    document.getElementById("output1").innerHTML = message[confirm_num]



