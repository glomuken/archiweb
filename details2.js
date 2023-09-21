<script>
document.addEventListener("DOMContentLoaded", function () {
  // Check if the user is logged in (you should implement this logic)
  var isLoggedIn = false; // Replace with your actual authentication logic

  // Get a reference to the "Details" button
  var detailsButton = document.getElementById("details2");

  // Add a click event listener to the "Details" button
  detailsButton.addEventListener("click", function () {
    if (isLoggedIn) {
      // If the user is logged in, redirect to the protected page
      window.location.href = "drawing_plan.html";
    } else {
      // If the user is not logged in, redirect to the login page
      window.location.href = "login.html";
    }
  });
});
</script>
