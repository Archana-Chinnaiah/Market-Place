const urlParams = new URLSearchParams(window.location.search);
const customer_id =urlParams.get('customer_id')
console.log(customer_id);

if (customer_id == null)
{
    window.location.replace(`C:/Users/PC/Desktop/full_html_js/login.html`)
}




function home()
{
    window.location.assign(`C:/Users/PC/Desktop/full_html_js/category.html?customer_id=${customer_id}`)
}

function cart()
{
    window.location.assign(`C:/Users/PC/Desktop/full_html_js/customer_cart.html?customer_id=${customer_id}`)
}

function logout()
{
    
    window.location.replace(`C:/Users/PC/Desktop/full_html_js/login.html`)
}




//fetching data
fetch("http://127.0.0.1:5000/categories")
    .then(resp => {
        resp.json()
    .then(data => {
        console.log(data);
        data.forEach(element => {
            createNode(element);
        }); 
    })
    .catch(er => {
        console.log("data error",er)
    })
    .catch(er =>
        {
            console.log("response error",er)
        }
        )
    });

//creating elements
  
function createNode(element){
    console.log("creation started")
  
    // const row = document.createElement('div')
    const column = document.createElement('div')
    const a = document.createElement('a')
    const names = document.createElement('div')
    const img = document.createElement('img')
    const name = document.createElement('h2')
    const description = document.createElement('h5')
    
  
    // row.setAttribute('class','row')
    column.setAttribute('class','col-md-5 category-card')
    names.setAttribute('class','names')
    img.setAttribute('src',`C:/Users/PC/Desktop/full_html_js/category/${element['category_id']}.jpg`)
    name.innerHTML=element['name']
    description.innerHTML=element['description']
    
    names.setAttribute('id',element['category_id'])
    names.setAttribute('onclick','item(id)')
  
    const center = document.getElementsByClassName('middle_page')[0];
    // center.append(row)
    center.append(column)
    column.append(a)
    a.append(names)
    names.append(img)
    names.append(name)
    names.append(description)
    console.log("created");
}

//assign next window
function item(category_id){ 
    console.log(category_id);
    console.log(customer_id);
    window.location.assign(`file:///C:/Users/PC/Desktop/full_html_js/item.html?category_id=${category_id}&customer_id=${customer_id}`)
  }    


