const urlParams = new URLSearchParams(window.location.search);
const customer_id =urlParams.get('customer_id')

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



fetch(`http://127.0.0.1:5000/cart/${customer_id}`)
  .then((res)=>{
      res.json().then((data) => {
        console.log(data)
          data.forEach(function(element){
            createNode(element);         
          });
            
          
      }).catch((jErr) => {
          console.log('catch', jErr)
      })
  })
  .catch((err)=>{
      console.log("err",err)
  })



  function createNode(element){


    console.log("cart_id",element['cart_id'])
    console.log("quantity",element['quantity'])
    console.log("item_id",element['item_id'])

    console.log("hi")
    const column = document.createElement('div')
    const name = document.createElement('h2')
    const totalprice = document.createElement('h3')
    const quantity = document.createElement('h3')
    const a = document.createElement('a')
    const img = document.createElement('img')
    const items = document.createElement('div')
    const quantity_need= document.createElement('input')
    const update_quantity = document.createElement('input')
    const delete_item = document.createElement('input')

    column.setAttribute('class','column')
    items.setAttribute('class','items')

    name.innerHTML=element['item_name']
    totalprice.innerHTML="Total Price= "+element['total_price']
    quantity.innerHTML="Quantity-"+element['quantity']
    
    img.setAttribute('src',`C:/Users/PC/Desktop/full_html_js/item/${element['item_id']}.jpg`)
    quantity_need.setAttribute('class',element['cart_id'])
    quantity_need.setAttribute('value',element['quantity'])
    quantity_need.setAttribute('placeholder','Enter the Quantity')

    console.log(img)

   update_quantity.setAttribute('class','update')
   update_quantity.setAttribute('type','submit')
   update_quantity.setAttribute('value','quantity')
   update_quantity.setAttribute('id',element['cart_id'])
   
   console.log("cart value",element['cart_id'])
   
   update_quantity.setAttribute('onclick','update_quantity(id)')

   delete_item.setAttribute('class','delete')
   delete_item.setAttribute('id',element['cart_id'])
   delete_item.setAttribute('value','delete')
   delete_item.setAttribute('type','submit')
   delete_item.setAttribute('onclick','delete_item(id)')

    const item = document.getElementsByClassName('middle_page')[0];
    item.append(column)
    column.append(a)
    a.append(items)
    items.append(img)
    items.append(name)
    items.append(quantity)
    items.append(totalprice)
    column.append(quantity_need)
    column.append(update_quantity)
    column.append(delete_item)
   
  }



function update_quantity(cart_id){
   
    console.log(cart_id)
    const result = document.getElementsByClassName(cart_id)[0].value
    console.log("result",result)
    
  fetch(`http://127.0.0.1:5000/cart/${cart_id}`,{
      method:'PUT',
      headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
      body:JSON.stringify({
        'quantity':result
    })
  }).then((res)=>{
      res.json()
      .then((data)=>{
        if(data['msg'] == 'updated'){
          alert('updated successfully')
          window.location.assign(`C:/Users/PC/Desktop/full_html_js/customer_cart.html?customer_id=${customer_id}`)
      }
      if(data['msg']== 'out of stock'){
        alert(data['msg'])
      }
    })
  })  

}


function delete_item(cart_id){

  console.log(cart_id)
  fetch(`http://127.0.0.1:5000/cart/${cart_id}`,{
      method:'DELETE',
      headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
      body:JSON.stringify({
        'cart_id':cart_id
    })
  })
 .then((res)=>{
      res.json()
      .then((data)=>{
        alert(data['msg'])
          console.log(data)
          window.location.assign(`C:/Users/PC/Desktop/full_html_js/customer_cart.html?customer_id=${customer_id}`)
  })
}
 )
}

  