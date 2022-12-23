

     //VARIABLES PARA LOS EVENTOS
     var next_click= document.querySelectorAll(".next_btn");
            
            
     var prev_click= document.querySelectorAll(".prev_btn");
     var sbmt_click= document.querySelectorAll(".sbmt_btn");
     var main_page= document.querySelectorAll(".main");
     var p_bar = document.querySelectorAll(".progres_bar li");
     var written_name= document.querySelector(".written_name");
     var shown_name= document.querySelector(".shown_name");
     
    //Para saber en que formulario estamos    
     let formnumber= 0;
     
     var passeye= document.querySelector(".password_eye");
     var pass_type= document.querySelector(".pass_type");
     var set_pass= document.querySelector(".password_eye");
     
     var confirm_passeye= document.querySelector(".con_eye");
     var confirm_pass_type= document.querySelector(".confirm_pass_type");
     var confirm_set_pass= document.querySelector(".con_eye");
     
     var tick= document.querySelector(".agree span");

     //EVENTOS JAVASCRIPT
     tick.addEventListener('click',function(){
         tick.classList.toggle('agree_green');
     });
     
     var tick_green= document.querySelector(".agree_submit span");
     tick_green.addEventListener('click',function(){
         tick_green.classList.toggle('agree_submit_green');
     });
     
     
     passeye.addEventListener('click',function(){
     
         if(pass_type.type=="password"){
             pass_type.type="text";
             set_pass.classList.remove('fa-eye-slash');
             set_pass.classList.add('fa-eye');
         }else{
             pass_type.type="password";
             set_pass.classList.add('fa-eye-slash');
             set_pass.classList.remove('fa-eye');
         }

     });
     
     
     confirm_passeye.addEventListener('click',function(){
     
         if(confirm_pass_type.type=="password"){
             confirm_pass_type.type="text";
             confirm_set_pass.classList.remove('fa-eye-slash');
             confirm_set_pass.classList.add('fa-eye');
         }else{
             confirm_pass_type.type="password";
             confirm_set_pass.classList.add('fa-eye-slash');
             confirm_set_pass.classList.remove('fa-eye');
         }

     });
     
     
     
     next_click.forEach(function(btn){

         btn.addEventListener('click',function(){


            //Validamos todos los campos
            if(!validate_form()){
                console.log("Estamos en el formulario",formnumber);
               return false;
            }


            if(formnumber == 0){
                console.log("Estamos en el primer formulario");

                if (input_password1.value == input_password2.value){
                    console.log("la calve esta igual");
                    input_password1.classList.remove('warning');
                    input_password1.classList.remove('warning');


                    /**AQUI VAMOS A USAR FETCH PARA LLAMAR A LA API DE CORREOS Y QUE LE ENVIE UN CODIGO */

                    console.log(formData);

                    var data = {
                    //'digitos': lista_digitos,
                    'correo': formData.get('emailUsuario'),
                    //'comprobante': formData.get('comprobante'),
                    };


                    //AQUI ES CUANDO ES POST
                    fetch("enviar_codigo_email/",{
                        method:"POST",
                        //body: formData,
                        body:JSON.stringify(data),
                        headers:{
                            'Content-Type': 'application/json',
                            "X-CSRFToken":csrftoken,
                            "X-Requestd-With":"XMLGttpRequest"//Con esto indicamos que es una peticion ajax
                        }

                    //Promesa de javascript
                    }).then(
                        function(response){

                            return response.json();
                            
                            //console.log(response.data);
                        }//fin de la funcion

                    ).then(
                        function(data){

                            //Esto es para saber la longitud del Json
                            //Object.keys(data).length

                            //En caso de que no haya ningun mensaje

                            if(Object.keys(data).length == 0){

                                console.log("No hay mensajes traidos de la api");
                            
                            }else{

                                console.log("Hay mensajes traidos de la api");
                                //console.log(Object.keys(data).length);
                                //MensajeSubliminal.classList.remove("d-none","alert-danger");
                                //MensajeSubliminal.classList.add("alert-primary"); //alert alert-success
                                //MensajeSubliminal.innerHTML = "Informacion:<br> ";
                                console.log("datos traidos desde la api: ",data);
                                console.log("tipo de dato: ",typeof data);
                                console.log("datos traidos desde la api: ",data['name']);

                            }//fin del else

                            


                        }//fin de la funcion(data)

                    ) //fin de then



                /**AQUI FINALIZAMOS CON LA FUNCION FETCH DE API CORREOS */



                }else{
                    console.log("la calve NO esta igual");
                    input_password1.classList.add('warning');
                    input_password2.classList.add('warning');
                    return 10;
                }

             }else if(formnumber == 1){
                console.log("Estamos en el segundo formulario");
             }

             

             
             formnumber++;
             update_form();
             progress_forward();
         });
     });
     

     prev_click.forEach(function(btn){
    
        btn.addEventListener('click',function(){
            formnumber--;
            update_form();
            progress_backward();
        });

     });
     
     sbmt_click.forEach(function(btn){

        btn.addEventListener('click',function(){
        if(!validate_form()){
            return false;
        }
        formnumber++;
        update_form();
        shown_name.innerHTML=written_name.value;

        });

     });
     
     function progress_forward(){

        p_bar[formnumber].classList.add('active');

     }
     
     function progress_backward(){

        var f_num = formnumber+1;
        p_bar[f_num].classList.remove('active');

     }
     
     
     
     function update_form(){

        main_page.forEach(function(main_pages){
        main_pages.classList.remove('active');
     
        });

        main_page[formnumber].classList.add('active');

     }
     
    function validate_form(){
        var validate=true;
        var all_inputs=document.querySelectorAll(".main.active input");
        all_inputs.forEach(function(inpt){

            inpt.classList.remove('warning');
            
            if(inpt.hasAttribute("required")){

                if(inpt.value.length=="0"){
                    validate=false;
                    inpt.classList.add('warning');
                }
            }
            });

        return validate;
    
    }