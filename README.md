{% load static %}
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
       
        .font{
            color: white;
        }
        .position{
            margin-top: 10%;
            text-align: center;
            font-family: serif;
            font-size:x-large;
        }
        .position2{
            margin: 50px;
            text-align: center;
        }
        .position3{
            margin-top: 150px;
            margin-left: 50px;
            margin-bottom: 50px;
            margin-right: 50px;
            text-align: center;
        }
        body{
            background-image: url('static/black-wallpaper-to-set-as-background-33.jpg');

        }
        a:link, a:visited {
            background-color: transparent;
            color: white;
            border: 2px solid white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            border-radius: 10px;
          }
          
          a:hover, a:active {
            background-color: white;
            color: black;
          }
        .arrangement{
            display:flex;
            margin-left: 25%;
            margin-right: 25%;
        }
        .container{
            margin-bottom: auto;
            margin-top: auto;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }
        a{
            text-decoration: none;
        }
        p{
            font-size: large;
            color: white;
        }
    </style>
    <title>Sparks Bank</title>
</head>
<body>

    <div>
        <div class="position">
            <h1 class="font">Sparks Bank</h1>
        </div>
    
        <div class="position2">
            <h3 class="font">Welcome to Sparks Bank.....!</h3>
        </div>
    
        <div class="arrangement">
          
            <div class="container">
                <a href="payments">Make Transaction</a></button>
            </div>
    
            <div class="container">
                <a href="history">Transaction History</a></button>
            </div>
    
            <div class="container">
                <a href="customers">Customer's Data</a></button>
            </div>
    
        </div>

    </div>
        <div class="position3">

            <p>&copy; Made By Rushikesh Lahole</p>

        </div>
        
</body>
</html>
