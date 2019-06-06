function validate(myform){
  var isValid=false;
  {% for credential in loginData %}
    if(myForm.user.value=="{{credential.User}}"&&myForm.password.value=="{{credential.Password}}"){
      isValid=true;
    }
  {% endfor %}
    alert(isValid)
}
