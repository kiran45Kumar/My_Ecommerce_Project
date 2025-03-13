
const carousel = document.querySelector(".carousel");
const cardWidth = document.querySelector(".card").clientWidth;
const totalCards = document.querySelectorAll(".card").length;
const input = document.getElementById("input");
const eye = document.getElementById("btn");
let doc = document.getElementsByClassName("form-input").length;
let message1 = "Login Successfull!!!";
let message2 = "SignUp Successfull!!!";
let search = document.getElementById("search2");
let cart1 = document.getElementById('cart');


function displayMessage() {

  let mail = document.getElementById("email");
  let password = document.getElementById("input");
  let message = document.getElementById("Login");
  if (mail.value === "") {
    message.innerHTML = "Enter Your Email!!!";
    message.style.color = "red";
  } else if (password.value == "") {
    message.innerHTML = "Enter Your Password!!!";
    message.style.color = "red";
  }
  else if (mail.value == 'admin@gmail.com' && password.value == 'admin1234') {
    message.innerHTML = 'Welcome Admin';
    message.style.color = 'green';
    window.location.href = 'admin.html'
  }
  else {
    message.innerText = `Login Successfull`;
    message.style.color = "green";
    message.style.fontWeight = "600";
    window.location.href = "/";
  }
}
function login() {
  window.location.href = '/'
}
function table() {
  window.location.href = 'table.html'
}
function displayMessage2() {

  let name = document.getElementById("Name");
  let phone = document.getElementById("phone");
  let mail = document.getElementById("email");
  let password = document.getElementById("input");
  let message = document.getElementById("Login");
  if (mail.value === "") {
    message.innerHTML = "Enter Your Email!!!";
    message.style.color = "red";
  } else if (password.value == "") {
    message.innerHTML = "Enter Your Password!!!";
    message.style.color = "red";
  } else if (name.value == "") {
    message.innerHTML = "Please Enter Your Name";
    message.style.color = "red";
  } else if (phone.value == "" || phone.value.length !== 10) {
    message.innerHTML = "Please Enter Your PhoneNo";
    message.style.color = "red";
  } else {
    message.innerText = `Signup Successfull`;
    message.style.color = "green";
    message.style.fontWeight = "600";
    window.location.href = "/login";
  }
}
function displayMessage3() {
  let name = document.getElementById("Name");
  let phone = document.getElementById("phone");
  let address = document.getElementById("address");
  let message = document.getElementById("Login");
  if (name.value == "") {
    message.innerHTML = "Please Enter Your Name";
    message.style.color = "red";
  } else if (phone.value == "" || phone.value.length !== 10) {
    message.innerHTML = "Please Enter Your PhoneNo";
    message.style.color = "red";
  } else if (address.value == "") {
    message.innerHTML = "Please Enter Your Address";
    message.style.color = "red";
  } else {
    message.innerText = `Account Created Now You Can Sell`;
    message.style.color = "green";
    message.style.fontWeight = "600";
    window.location.href = "/create";
  }
}
function checkout() {
  window.location.href = '/checkout'
}
function billing() {
  window.location.href = '/billing';
}
function dashboard() {
  window.location.href = '/admind';
}
function delivery() {
  window.location.href = '/delivery';
}
function create() {
  let gname = document.getElementById("gname");
  let brand = document.getElementById("brand");
  let category = document.getElementById("category");
  let price = document.getElementById("price");
  let quantity = document.getElementById("quantity");
  let dosage = document.getElementById("Dosage");
  let Composition = document.getElementById("Composition");
  let Indications = document.getElementById("Indication");
  let ContraIndications = document.getElementById("Contra");
  let SideEffects = document.getElementById("side");
  let Barcode = document.getElementById("barcode");
  let message = document.getElementById("Login");
  let medprice = document.getElementById("med-price");
  let title = document.getElementById("medicine-title");
  let gname1 = document.getElementById("gname").value;
  let price1 = document.getElementById("price").value;
  const medname = localStorage.setItem('gname', gname1);
  const medp = localStorage.setItem('price', price1)
  if (gname.value == "") {
    message.innerHTML = "Please Enter Generic Name";
    message.style.color = "red";
  } else if (brand.value == "") {
    message.innerHTML = "Please Enter Brand Name";
    message.style.color = "red";
  } else if (category.value == "") {
    message.innerHTML = "Please Enter Category";
    message.style.color = "red";
  } else if (price.value == "") {
    message.innerHTML = "Price??";
    message.style.color = "red";
  } else if (quantity.value == "") {
    message.innerHTML = "Quantity??";
    message.style.color = "red";
  } else if (dosage.value == "") {
    message.innerHTML = "Please Enter Dosage Form";
    message.style.color = "red";
  } else if (Composition.value == "") {
    message.innerHTML = "Please Enter Composition";
    message.style.color = "red";
  } else if (Indications.value == "") {
    message.innerHTML = "Please Enter Indications";
    message.style.color = "red";
  } else if (ContraIndications.value == "") {
    message.innerHTML = "Please Enter ContraIndications";
    message.style.color = "red";
  } else if (SideEffects.value == "") {
    message.innerHTML = "Please Enter SideEffects";
    message.style.color = "red";
  } else if (Barcode.value == "") {
    message.innerHTML = "Please Enter The Barcode";
    message.style.color = "red";
  } else {
    message.innerText = `Order Created Now You Can Sell`;
    message.style.color = "green";
    message.style.fontWeight = "600";
    const medn = localStorage.getItem('gname', medname)
    const medp1 = localStorage.getItem('price', medp)
    window.location.href = "medicine.html";
    title.innerHTML = `${medn}`
    medprice.innerHTML = `${medp1}`
  }
}
function submit() {
  let email = document.getElementById("email");
  let input = document.getElementById("input");
  if (email.value === "" || input.value === "") {
    alert("Please Enter Your Email Address and Passowiord");
  }
}
function cart(customer) {
  window.location.href = '/cart_page/' + encodeURIComponent(customer)
}
let currentIndex = 0;

document.getElementById("right").addEventListener("click", () => {
  if (currentIndex < totalCards - 1) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  carousel.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
});

document.getElementById("left").addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
  } else {
    currentIndex = totalCards - 1;
  }
  carousel.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
});

function showIcon() {
  let icon = document.getElementById("eye");
  let input = document.getElementById("input");
  if (icon.classList.contains("fa-eye-slash")) {
    icon.classList.remove("fa-eye-slash");
    icon.classList.add("fa-eye");
    input.type = "password";
  } else if (icon.classList.contains("fa-eye")) {
    icon.classList.remove("fa-eye");
    icon.classList.add("fa-eye-slash");
    input.type = "text";
  }
}
function checkout() {
  let user = document.getElementById('user')
  let phone = document.getElementById('userphone')
  let email = document.getElementById('usergmail')
  let address = document.getElementById('useraddress')
  let useralternate = document.getElementById('useralternate')
  let landmark = document.getElementById('userlandmark')
  let city = document.getElementById('usercity')
  let state = document.getElementById('userstate')
  let pincode = document.getElementById('userpostalcode')
  let message = document.getElementById("Login");
  if (user.value == '' || email.value == '' || address.value == '' || useralternate.value == '' || landmark.value == '' || city.value == '' || state.value == '' || pincode.value == '') {
    message.innerHTML = 'Please Fill All the fields '
    message.style.color = 'red'
  }
  else if (phone.value.length !== 10) {
    message.innerHTML = 'Phone Number Length Should be 10'
    message.style.color = 'red'
  }
  else {
    message.innerHTML = 'Thanks'
    message.style.color = 'green'
    window.location.href = '#payment'
  }

}

function payment() {
  let credit = document.getElementById('credit');
  let cvv = document.getElementById('cvv');
  let expiry = document.getElementById('expiry');
  let message = document.getElementById("Login2");
  if (credit.value == '') {
    message.innerHTML = 'Please Enter Your Credit Card Number'
    message.style.color = 'red'
  }
  else if (credit.value.length !== 16) {
    message.innerHTML = 'Please Enter a Valid Credit Card Number'
    message.style.color = 'red'
  }
  else if (cvv.value == '') {
    message.innerHTML = 'Enter Your CVV'
    message.style.color = 'red'
  }
  else if (expiry.value == '') {
    message.innerHTML = 'Enter Your Expiry'
  }
  else {
    message.innerHTML = 'Thanks for Submitting';
    message.style.color = 'green'
  }
}
function signup() {
  window.location.href = 'signup.html'
}
function sellnow() {
  window.location.href = '/sell'
}
function medicine() {
  window.location.href = '/medicines'
}

function successMessage() {
  let mail = document.getElementById('footer-mail');
  let success = document.getElementById('success');
  if (mail.value == '') {
    success.innerHTML = 'Please Enter Your Email'
    success.style.color = 'red'
  }
  else if (!mail.value.includes('@')) {
    success.innerHTML = 'Please Enter a Valid Email Address'
    success.style.color = 'red'
  }
  else {
    success.innerHTML = 'Thanks for Subscription';
    success.style.color = 'green';
  }
}
// add vendor role = admin
function addVendor() {
  let supplier_name = $("#supplier_name").val();
  let phone_number = $("#phone_number").val();
  let email = $("#email").val();
  let CompanyName = $("#CompanyName").val();
  let CompanyGst = $("#CompanyGst").val();
  let address = $("#address").val();

  $.ajax({
    type: "POST",
    url: "/addVendor/",
    data: {
      "supplier_name": supplier_name,
      "phone_number": phone_number,
      "email": email,
      "CompanyName": CompanyName,
      "CompanyGst": CompanyGst,
      "address": address,
    },
    success: function (data) {
      if (data.status == 'pass') {
        // Show Success Toast
        const successToast = new bootstrap.Toast(document.getElementById('successToast'));
        successToast.show();

        // Optional: Reload page after showing toast
        setTimeout(function () {
          window.location.reload();
        }, 2000); // 2-second delay before reload
      } else {
        // Show Error Toast
        const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
        $("#errorToast .toast-body").text('Failed to add vendor.');
        errorToast.show();
      }
    },
    error: function (xhr, status, error) {
      // Show Error Toast
      const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
      $("#errorToast .toast-body").text('An error occurred. Please try again.');
      errorToast.show();
    }
  });
}
function addMedicine() {
  let generic_name = $("#generic_name").val();
  let med_image = $("#med_image")[0].files[0];
  let brand_name = $("#brand_name").val();
  let category = $("#category").val();
  let dosage_form = $("#dosage_form").val();
  let quantity = $("#quantity").val();
  let price = $("#price").val();
  let composition = $("#composition").val();
  let Indications = $("#quantity").val();
  let contraindications = $("#contraindications").val();
  let side_effects = $("#side_effects").val();
  let supplier_vendor = $("#supplier_vendor").val();
  let barcode = $("#barcode").val();

  const formdata = new FormData();
  formdata.append('generic_name',generic_name)
  formdata.append('med_image',med_image)
  formdata.append('brand_name',brand_name)
  formdata.append('category',category)
  formdata.append('dosage_form',dosage_form)
  formdata.append('quantity',quantity)
  formdata.append('price',price) 
  formdata.append('composition',composition) 
  formdata.append('Indications',Indications) 
  formdata.append('contraindications',contraindications) 
  formdata.append('supplier_vendor',supplier_vendor) 
  formdata.append('side_effects',side_effects) 
  formdata.append('barcode',barcode) 
  $.ajax({
    type: "POST",
    url: "/add_medicine_api/",
    data:formdata,
    processData:false,
    contentType:false,
    success: function (data) {
      if (data.status == 'pass') {
        // Show Success Toast
        const successToast = new bootstrap.Toast(document.getElementById('successToast'));
        successToast.show();

        // Optional: Reload page after showing toast
        setTimeout(function () {
          window.location.reload();
        }, 2000); // 2-second delay before reload
      } else {
        // Show Error Toast
        const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
        $("#errorToast .toast-body").text('Failed to add vendor.');
        errorToast.show();
      }
    },
    error: function (xhr, status, error) {
      // Show Error Toast
      const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
      $("#errorToast .toast-body").text('An error occurred. Please try again.');
      errorToast.show();
    }
  });
}
function UpdateVendor(id) {
  let supplier_name = $("#supplier_name"+id).val();
  let supplier_phone = $("#supplier_phone"+id).val();
  let supplier_email = $("#supplier_email"+id).val();
  let CompanyName = $("#CompanyName"+id).val();
  let CompanyGst = $("#CompanyGst"+id).val();
  let supplier_address = $("#supplier_address"+id).val();
  let account_created_by = $("#account_created_by"+id).val();

  $.ajax({
    type: "POST",
    url: "/update_vendor_api/",
    data: {
      "id":id,
      "supplier_name": supplier_name,
      "supplier_phone": supplier_phone,
      "supplier_email": supplier_email,
      "CompanyName": CompanyName,
      "CompanyGst": CompanyGst,
      "supplier_address": supplier_address,
      "account_created_by": account_created_by,
    },
    success: function (data) {
      if (data.status == 'pass') {
        // Show Success Toast
        const successToast = new bootstrap.Toast(document.getElementById('successToast'));
        successToast.show();
        setTimeout(function () {
          window.location.replace('/update_vendor_admin/');
        }, 2000); // 2-second delay before reload
      } else {
        // Show Error Toast
        const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
        $("#errorToast .toast-body").text('Failed to add vendor.');
        errorToast.show();
      }
    },
    error: function (xhr, status, error) {
      // Show Error Toast
      const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
      $("#errorToast .toast-body").text('An error occurred. Please try again.');
      errorToast.show();
    }
  });
}
// remove vendor role = admin
function RemoveSeller(id) {
  $.ajax({
    type: "POST",
    url: "/remove_vendor_admin/",
    data: {
      "id": id,
    },
    success: function (response) {
      if (response.status == 'pass') {
        // Show success toast
        const successToast = new bootstrap.Toast(document.getElementById('successToast'));
        successToast.show();
        setTimeout(function () {
          window.location.reload();
        }, 2000);
      } else {
        const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
        $("#errorToast .toast-body").text('Failed to remove seller.');
        errorToast.show();

        setTimeout(function () {
          window.location.reload();
        }, 2000);
      }
    },
    error: function (xhr, status, error) {
      const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
      $("#errorToast .toast-body").text('Oops! Something went wrong.');
      errorToast.show();

      setTimeout(function () {
        window.location.reload();
      }, 2000);
    }
  });
}
function UpdateVendorForm(id) { 
  window.location.replace('/update_vendor_form/'+encodeURIComponent(id))
 }
 function RemoveMedicine(id) {
  $.ajax({
    type: "POST",
    url: "/remove_medicine_api/",
    data: {
      "id": id,
    },
    success: function (response) {
      if (response.status == 'pass') {
        // Show success toast
        const successToast = new bootstrap.Toast(document.getElementById('successToast'));
        successToast.show();
        setTimeout(function () {
          window.location.reload();
        }, 2000);
      } else {
        const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
        $("#errorToast .toast-body").text('Failed to remove seller.');
        errorToast.show();

        setTimeout(function () {
          window.location.reload();
        }, 2000);
      }
    },
    error: function (xhr, status, error) {
      const errorToast = new bootstrap.Toast(document.getElementById('errorToast'));
      $("#errorToast .toast-body").text('Oops! Something went wrong.');
      errorToast.show();

      setTimeout(function () {
        window.location.reload();
      }, 2000);
    }
  });
}