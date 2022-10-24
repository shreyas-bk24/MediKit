var first_name=document.getElementById('firstname').value;
var last_name=document.getElementById('lastname').value;
var email=document.getElementById('email').value;
var password1=document.getElementById('password').value;
var password2=document.getElementById('password2').value;

// validations for first name
var firstname_val=()=>{
if((first_name.length)<2){
    document.getElementById('fname_message').innerHTML="Enter a Valid first name";
    
}   
}

// validations for lastname
var lastname_val=()=>{
    if(last_name=="" | last_name==none){
        document.getElementById('lname_err').innerHTML="last name is required";
    }
}

// validations for email

var validate_email=(email)=>{
    if(/^\w+([\.-]?\w)*@\w+)*(\.\w{2,3})+$/.test(email)){
        return true;
    }
    else{
        document.getElementById('email_err').innerHTML('Enter a valid email id')
    }
}

