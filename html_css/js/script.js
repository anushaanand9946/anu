function Read(){
    var name=document.getElementById("getname").value;
    

    var rollno=document.getElementById("getrollno").value;
    

    var admnno=document.getElementById("getadmnno").value;
    
    var age=document.getElementById("getage").value;
    
    var op=document.getElementById("district");
    var district=op.options[op.selectedIndex].value;
    
    console.log(name);
    console.log(rollno);
    console.log(admnno);
    console.log(age);
    console.log(district);

   
    if(age>=18)
    {
        console.log("Eligible");
        alert("Eligible")
    }
    else{
        console.log("NotEligible");
        alert("NotEligible")
    }

}



function addition()
{
    var num1=document.getElementById("op1").value;
    var num2=document.getElementById("op2 ").value;

    var x = parseInt(num1);
    var y = parseInt(num2);


    var num3= x+y;
    console.log(num3)
}


