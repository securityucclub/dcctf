<?php
    include "flag.php";
    session_start();

    function generateRandomString($length = 40) {
        $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }
        return $randomString;
    }

    $token = generateRandomString();

    $h = $_SERVER["CONTENT_TYPE"];
    if (isset($_POST['Submit'])){
        $data = $_POST["input"];
        if ($data == $token) {
            echo $flag;
        }
        else {
            echo "Password incorrecta\n";
        }
    }
    else if (strpos($h, 'json') !== false) {
        $data = json_decode(file_get_contents('php://input'), true)["input"];
        if ($data == $token) {
            echo $flag;
        }
        else {
            echo "Password incorrecta\n";
        }
    }


?>
<title>Buscando el hash?</title>
<body bgcolor="">
<form action="" method="post" name="Login_Form">
  <table width="400" border="0" align="center" cellpadding="5" cellspacing="1" class="Table">
    <?php if(isset($msg)){?>
    <tr>
      <td colspan="2" align="center" valign="top"><?php echo $msg;?></td>
    </tr>
    <?php } ?>
    <tr>
      <td align="right" valign="top">Introduzca su Password</td>
      <td><input name="input" type="text" class="input"></td>
    </tr>
    <tr>
      <td> </td>
      <td><input name="Submit" type="submit" value="Login" class="Button3"></td>
    </tr>
  </table>
</form>
</body>
