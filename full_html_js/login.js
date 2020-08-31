var form=document.getElementById('form-style')
form.addEventListener('submit',function(e){
    e.preventDefault()
    var username = document.getElementById('username').value
    console.log("hi");
    var password=document.getElementById('password').value
    console.log("helo");
console.log(username)
console.log(password)

//fetch data
    fetch('http://127.0.0.1:5000/login', {
    method:'POST',
    body:JSON.stringify({
        username:username,
        password:password}),
    headers:{
    "Content-Type":"application/json ; charset=UTF-8"
    }
    })
    .then(function(response){
        return response.json()
        })
        .then(function(data){
            console.log(data)
            if(data['status'] == '200'){
            console.log(data['customer_id'])
                   window.location.replace(`C:/Users/PC/Desktop/full_html_js/category.html?customer_id=${data['customer_id']}`)
                }
                    else{
                        alert('Invalid Credentials')
                    }        
                })

})