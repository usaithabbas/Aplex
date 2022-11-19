<?php
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$email = $_POST['email'];
$feedback = $_POST['feedback'];

if (!empty($firstname) || !empty($lastname) || !empty($email) || !empty($feedback)){
  $host = "localhost";
  $dbusername = "root";
  $dbpassword = "";
  $dbname = "form";

  $conn = new mysqli($host, $dbusername, $dbpassword, $dbname);

  if (mysqli_connect_error()){
    die('connect error('. mysqli_connect_error().')')
  }
  else{
    $SELECT = "SELECT email from register where email = ? limit 1";
    $INSERT = "INSERT Into register (firstname, lastname, email, feedback) values(?, ?, ?, ?)";

    $stmt = $conn->prepare($SELECT)
    $stmt->blind_param("s", $email);
    $stmt->execute();
    $stmt->blind_result($email);
    $stmt->store-result();
    $rnum = $stmt->num_rows;

    if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->blind_param("ssssii", $firstname, $lastname, $email, $feedback);
      $stmt->execute();
      echo "new record inserted successfully";
    }
    else{
      echo "Someone already registered in this email";
    }
    $stmt->close();
    $stmt->close();
  }
}
else{
  "All the field are required.";
  die();
}

 ?>
