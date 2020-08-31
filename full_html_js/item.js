const urlParams = new URLSearchParams(window.location.search);
const category_id =urlParams.get('category_id')
const customer_id =urlParams.get('customer_id')

console.log(category_id);
console.log(customer_id);

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

//fetching items
fetch(`http://127.0.0.1:5000/categories/${category_id}/items`)
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

  function createNode(element){
      
    console.log("creation started")
  
    const column = document.createElement('div')
    const name = document.createElement('h2')
    const price = document.createElement('h3')
    const available_quantity = document.createElement('h3')
    const seller_name = document.createElement('h3')
    const description = document.createElement('h3')
    const a = document.createElement('a')
    const img = document.createElement('img')
    const items = document.createElement('div')
    const add_to_cart= document.createElement('input')
    
    console.log("creation finished")
    
    column.setAttribute('class','column col-md-4')
    items.setAttribute('class','items')
    add_to_cart.setAttribute('class','btn btn-primary')
    img.setAttribute('src',`C:/Users/PC/Desktop/full_html_js/item/${element['item_id']}.jpg`)
    
    add_to_cart.setAttribute('id','add_to_cart')
    add_to_cart.setAttribute('type','submit')
    add_to_cart.setAttribute('value','Add-to-cart')
    add_to_cart.setAttribute('id',element['item_id'])

    
    name.innerHTML=element['name']
    price.innerHTML="Price- "+element['price']
    available_quantity.innerHTML="quantity- "+element['available_quantity']
    seller_name.innerHTML="seller name-"+element['seller_name']
    description.innerHTML="description -"+element['description']
    
    console.log("id",element['item_id']);

    add_to_cart.setAttribute('onclick','add_to_cart(id)')
    
    const item = document.getElementsByClassName('middle_page')[0];
    item.append(column)
    column.append(a)
    a.append(items)
    items.append(img)
    items.append(name)
    items.append(price)
    items.append(available_quantity)
    items.append(seller_name)
    items.append(description)
    column.append(add_to_cart)

    console.log("created")
   
  }

function add_to_cart(item_id)
{
    console.log(item_id);
    console.log(customer_id);
    fetch(`http://127.0.0.1:5000/cart`,{
    method:'POST',
    headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
    body:JSON.stringify({
        customer_id:customer_id,
        item_id:item_id    
    })
}).then((res)=>{
    res.json()
    .then((data)=>{
        if(data['message'] == 'exsists'){
            alert('data already exsists')
            window.location.assign(`C:/Users/PC/Desktop/full_html_js/customer_cart.html?customer_id=${data['customer_id']}`)
        
            } 
            else if(data['message'] == 'out of stock'){
                alert('Out of stock');
            }
            else{
                console.log(data);
                alert('added successfully')
                window.location.assign(`C:/Users/PC/Desktop/full_html_js/customer_cart.html?customer_id=${data['customer_id']}`)
            }  
    })
} )}