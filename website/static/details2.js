<script>
document.addEventListener("DOMContentLoaded", function () {
  var isLoggedIn = false; 


  var detailsButton = document.getElementById("details2");

  
  detailsButton.addEventListener("click", function () {
    if (isLoggedIn) {
      
      window.location.href = "drawing_plan.html";
    } else {
      
      window.location.href = "login.html";
    }
});
});
</script>
