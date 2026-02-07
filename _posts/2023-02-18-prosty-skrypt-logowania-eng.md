---
title: "PHP+MySQL - Simple login script [ENG 🇬🇧]"
date: 2023-02-18
categories: 
  - "tutorials"
tags: 
  - "bloglab"
  - "cookies"
  - "hash"
  - "mysql"
  - "opensource"
  - "password"
  - "passwordhash"
  - "php"
  - "pregmatch"
  - "proofofconcept"
  - "script"
  - "session"
image: "/images/loginscript.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/prosty-skrypt-logowania/)

The idea for this post came to me while working on my new small project, which should see the light of day in the near future. The culmination of the following discourse will be the creation of a simple login script for use on any website. We will create a MySQL database to store user information, a script to create new accounts, and a script for logging in, or gaining access to protected content. This will be a Proof of Concept solution, meaning I will focus on the essential minimum, and leave further customization to the reader's specific needs.

## Demo page

For the purpose of this post, I have created something called _bloglab1_, which is a **test environment** to demonstrate the functioning of the mechanism that I will describe shortly. Access to the demo can be obtained by clicking on [this link](https://blog.tomaszdunia.pl/bloglab/lab1/login.php).

## MySQL user database - lab1\_users\_db.sql

To store user data, we need a **MySQL database**. Since we are focusing only on the basics, we will name our database _lab1\_users\_db_ and it will consist of only three columns storing:

- unique **ID** of the user, which will also be the _primary key_ for the database,

- **user** login,

- **password** of the user in hashed form, meaning a form that allows for unambiguous verification of a user who knows the correct password, but at the same time, a form that obtaining it will not reveal the actual password.

The subject of the password is a bit complicated, but in brief, _hashing_ is about not having access to the user's "plain" password as an administrator, while being able to properly verify/authenticate it. One-way encryption is used for this purpose, or rather I would call it (theoretically) irreversible, meaning that from a certain string of characters (the password in plain and understandable form for the user), through an appropriate encryption algorithm, a _hash_ is created, which looks like a string of completely random characters of relatively large length, which cannot be converted back to plain form, or at least it is not possible with the current state of technology, i.e. computing power of computers. Such a _hash_ is saved in the database during the creation of the account. The later verification consists of the user providing the password at each login, the server converts it to _hash A_, retrieves _hash B_ created during the account creation from the MySQL database, and compares the two. If they match (_A==B_), the user is authenticated.

We have the theories behind us, now let's create a database to store user data. The following code is a ready-made command for creating a properly configured database for the purposes of this guide. Such a database can also be created manually, for example in the _phpMyAdmin_ panel.

```sql
CREATE TABLE `lab1_users_db` (
  `id` int(11) NOT NULL,
  `login` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hashed_password` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;
ALTER TABLE `lab1_users_db`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `lab1_users_db`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
```

## Registration script - signup.php

In this script, there are basically **two interesting parts**:

- **lines 43-50** - verification of compliance with the requirements provided during registration of the login and password,

- **lines 63-69** - creating a hash of the password entered by the user for encryption.

To validate the correctness of the login and password, we use regular expressions (regexp), which I already mentioned in [one of my previous posts](https://blog.tomaszdunia.pl/twittodon-eng/). First, we had to define what our users' logins and passwords should look like. In my opinion, a reasonable approach for the login is to allow a string of 3 to 20 characters, which can consist of uppercase and lowercase letters, digits, and two special characters - hyphen (-) and underscore (\_). On the other hand, the password should be a string of 8 to 64 characters and consist of uppercase and lowercase letters, digits, and a slightly larger group of special characters - ! @ # $ % ^ & \*. Additionally, for the password, I forced the user to use at least one character from each of the mentioned groups. These regular expressions can be passed as arguments to the _preg\_match()_ function, which will do the rest of the work for us. If the login/password matches the specified regular expression, the function will return a value of _1_ (_true_), while if something does not match, it will return _0_ (_false_).

Let's now discuss the section concerning password hashing. We use the password\_hash() function for this, for which we must provide three arguments:

- **encryption password** - in our case, it is the content of the _$password_ variable obtained from the user using a text field in the registration form,

- **encryption algorithm** - we use _PASSWORD\_BCRYPT_, which is the _CRYPT\_BLOWFISH_ algorithm that always returns a string of 60 characters as a result,

- **options set** - consisting of two parameters: _cost_ which determines the level of complexity with which encryption is to be performed (must be selected according to the computing power of the encrypting unit), and _salt_ which is a string of characters added before encryption to make dictionary attacks (a type of brute force attack) more difficult.

```php
<?php
    include("[path to MySQL database login file]");
	
	header('Content-Type: text/html; charset=utf-8');
	$mysqli = mysqli_connect($host, $user, $pass, $db);
	mysqli_set_charset($mysqli, "utf8");
    // Initialize a new session or load an existing one
	session_start();
    // If there are variables with information about the username and hashed password in the session, then ...
    if(isset($_SESSION['login']) AND isset($_SESSION['hashed_password']))
    {
        // ... check if there is a record in the database containing these two values
		$login = addslashes(strip_tags($_SESSION["login"]));
		$hashed_password = addslashes(strip_tags($_SESSION['hashed_password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."' AND hashed_password = '".$hashed_password."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
		// If it exists, then ...
        if(!empty($db_users))
        {
            // ... skip the login process and redirect to protected content
            header("Location: secret.php");
        }
        else
        {
            // However, if there is no such record, destroy the current session and redirect to the login panel
            session_unset();
            session_destroy();
            header("Location: login.php");
        }
    }
	
	// If the Sign up button is pressed (meaning that the registration form has been submitted)
    if(isset($_POST['signup']))
    {
        // Set an empty alert variable
        $alert = "";
		// Perform a verification process of the correctness of the given username and password
        $login = addslashes(strip_tags($_POST['login']));
		$password = addslashes(strip_tags($_POST['password']));
		// Requirements for the username - length of 3-20 characters, upper and lower case letters, digits and special characters "_-"
		$check_login = '/^[A-Za-z0-9_-]{3,20}$/';
		// Requirements for the password - length of 8-64 characters, at least one uppercase and lowercase letter, at least one digit, and at least one special character from the allowed list "!@#$%^&*"
		$check_password = "/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*]).{8,64}$/";
        if(preg_match($check_login, $login))
        {
			if(preg_match($check_password, $password))
			{
				// If the username and password meet the requirements, then check if there is no user with this name in the database
				$query = "SELECT * FROM lab1_users_db WHERE login = '".$login."'";
				$result = mysqli_query($mysqli, $query);
				$db_users = mysqli_fetch_assoc($result);
				if(!empty($db_users))
				{
					// If there is, then display an error
					$alert = "User with that name already exists!";
				}
				else
				{
					// If there is no such user yet, then ...
					// Set options for the password encryption algorithm (hash creation)
					$options = [
						'cost' => 10,
						'salt' => 'secret_salt'
					];
					// Create a hash
					$hashed_password = password_hash($password, PASSWORD_BCRYPT, $options);
					// Insert a new record into the database
					$add = "INSERT INTO lab1_users_db (login, hashed_password) VALUES ('".$login."', '".$hashed_password."')";
					mysqli_query($mysqli, $add);
					// Redirect to the login panel
					header("Location: login.php");
				}
			}
			else
			{
				// If the password does not meet the requirements, it displays an error message
				$alert = "Invalid password! It needs to be 8-64 length, have at least one lower and upper case letters, number and special character (allowed: !@#$%^&*)";
			}
		}
		else
		{
			// If the login does not meet the requirements, it displays an error message
			$alert = "Invalid login! It needs to be 3-20 length and contains only allowed characters: a-z, A-Z, 0-9, special chars '_-'";
		}
    }
?>
<!-- HTML part (form) -->
<h1>CREATE ACCOUNT</h1>
<form action="" method="post">
	<p><input type="text" name="login" value="" placeholder="Login..." autocomplete="off"></p>
	<p><input type="password" name="password" value="" placeholder="Password..." autocomplete="off"></p>
	<p><button type="submit" name="signup">Sign up</button></p>
</form>
<p><a href="login.php">Already have account? Log in instead!</a></p>
<?php
	if($alert != "")
	{
		echo "<p>".$alert."</p>";
	}
?>
<p>Made for this blog post: <a href="https://blog.tomaszdunia.pl/prosty-skrypt-logowania/">https://blog.tomaszdunia.pl/prosty-skrypt-logowania/</a></p>
```

## Login script - login.php

With this script, I would like to delve into the topic of what a _session_ is, which is crucial for the login mechanism I am creating. So, a _session_ is mainly needed so that **the user does not have to log in again every time he refreshes the page**. Within the scope of the _session_, we keep information that this particular individual has already authenticated themselves and as long as their assigned _session_ has not expired, their identity is confirmed, and therefore we can serve them protected content that is intended for them. We will manage the session using three main commands:

- **session\_start()** - initializes a new or loads an existing _session_,

- **session\_unset()** - clears variables of a given _session_,

- **session\_destroy()** - removes all data from the given _session_, effectively destroying it.

Within a session, we can define and use so-called **global variables**, which are available between individual script executions (e.g. page refresh). They are stored in the _$\_SESSION_ array. These variables are stored on the server side, so **the user cannot manipulate their contents**. Only the session identifier, which allows correlation between the user and session, is stored on the user's side (browser).

```php
<?php
    include("[path to MySQL database login file]");
    header('Content-Type: text/html; charset=utf-8');
    $mysqli = mysqli_connect($host, $user, $pass, $db);
	mysqli_set_charset($mysqli, "utf8");
    // Initializing a new session or loading an existing one
	session_start();
    // If session variables with user name and hashed password exist, then ...
    if(isset($_SESSION['login']) AND isset($_SESSION['hashed_password']))
    {
        // ... checks if there is a record in the database containing these two values
        $login = addslashes(strip_tags($_SESSION['login']));
        $hashed_password = addslashes(strip_tags($_SESSION['hashed_password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."' AND hashed_password = '".$hashed_password."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
        // If such a record exists, then ...
        if(!empty($db_users))
        {
            // ... skips the login process and immediately redirects to protected content
            header("Location: secret.php");
        }
        else
        {
            // Otherwise, destroys the current session and redirects to the login panel
            session_unset();
            session_destroy();
            header("Location: login.php");
        }
    }
    // If the Sign in button has been pressed (meaning that the login form has been submitted)
    if(isset($_POST['signin']))
    {
        // Sets an empty variable called alert
        $alert = "";
        // Retrieves user data from MySQL database
        $login = addslashes(strip_tags($_POST['login']));
        $password = addslashes(strip_tags($_POST['password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
        // Checks if such a user exists at all
        if(empty($db_users))
        {
            // If there is no feedback data from the database, it means that the user does not exist
            $alert = "There is no such user!";
        }
        else
        {
           // If the user exists, it verifies the compatibility between the entered password and the password hash retrieved from the database
            if(password_verify($password, $db_users['hashed_password']))
            {
                // If they are compatible, it sets session variables and redirects to the protected content
                $_SESSION['login'] = $login;
                $_SESSION['hashed_password'] = $db_users['hashed_password'];
                header("Location: secret.php");
            }
            else
            {
                // If they are not compatible, it displays an error
                $alert = "Invalid password!";
            }
        }
    }
?>
<!-- HTML section (login form) -->
<h1>LOGIN</h1>
<form action="" method="post">
	<p><input type="text" name="login" value="" placeholder="Login..." autocomplete="off"></p>
	<p><input type="password" name="password" value="" placeholder="Password..." autocomplete="off"></p>
	<p><button type="submit" name="signin">Sign in</button></p>
</form>
<p><a href="signup.php">Don't have account? Create it!</a></p>
<?php
	if($alert != "")
	{
		echo "<p>".$alert."</p>";
	}
?>
<p>Made for this blog post: <a href="https://blog.tomaszdunia.pl/prosty-skrypt-logowania/">https://blog.tomaszdunia.pl/prosty-skrypt-logowania/</a></p>
```

## Protected content - secret.php

We have reached our mythical _protected value_! In this script, nothing too exciting happens. At the beginning, we check if there are variables in the session that allow us to access specific data from the MySQL database. If so, we display them. However, if anything goes wrong, we redirect the users directly to the login panel to authenticate themselves properly.

```php
<?php
    include("[path to MySQL database login file]");
    header('Content-Type: text/html; charset=utf-8');
	$mysqli = mysqli_connect($host, $user, $pass, $db);
	mysqli_set_charset($mysqli, "utf8");
	// Initializes a new session or loads an existing one
	session_start();
    
    // If there are variables in the session containing the username and hashed password, then ...
    if(isset($_SESSION['login']) AND isset($_SESSION['hashed_password']))
    {
        // ... checks in the database if there is a record containing these two values
        $login = addslashes(strip_tags($_SESSION['login']));
        $hashed_password = addslashes(strip_tags($_SESSION['hashed_password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."' AND hashed_password = '".$hashed_password."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
        // If it exists, then ...
        if(!empty($db_users))
        {
            // ... displays the protected content
            echo "<p>This is secret content page! You can access it only after a successful log in.</p>";
            echo "<p>Your login is: ".$db_users['login']."</p>";
            echo "<p>Your hashed password is: ".$db_users['hashed_password']."</p>";
            echo "<p><a href=\"logout.php\">Log out</a></p>";
        }
        else
        {
            // However, if there is no such record, it destroys the current session and redirects to the login panel
            session_unset();
            session_destroy();
            header("Location: login.php");
        }
    }
    else
    {
        header("Location: login.php");
    }
?>
<p>Made for this blog post: <a href="https://blog.tomaszdunia.pl/prosty-skrypt-logowania/">https://blog.tomaszdunia.pl/prosty-skrypt-logowania/</a><p>
```

## Logout script - logout.php

The shortest script in the comparison, but not the least important. It allows the user to log out informally, and in practice erases the entire current _session_, forcing a new login to access protected data.

```php
<?php
    // Initializes a new session or loads an existing one
    session_start();
    // Clears all session variables
    session_unset();
    // Deletes all session data
    session_destroy();
    // Redirects to the login panel
    header("Location: login.php");
?>
```

## Does this script use cookies?

If you are reading this post, dear Reader, you have probably seen at least one of my projects, so you probably know that I strive to make each of them open-source, transparent, and in the most possible way **caring for user privacy**. This involves the use of _cookies_, which unfortunately are a double-edged sword, because on the one hand they make our online life more **convenient**, for example by not having to authenticate our identity (log in) every time we refresh a page, but on the other hand they are **tragic in terms of privacy**. The main issue is that a misconfigured web browser can send all the _cookies_ collected on our device to websites that are not the owners of those _cookies_. Based on this, those websites can **effectively profile us**, and even obtain significant data about our behavior in other places on the internet. An example of this could be profiling and displaying subliminal ads based on what we read or buy online.

Why am I writing about this? One of the foundations of the solution described in this post is the use of a _session_, which is a kind of cousin to _cookies_. Both of these solutions are used to store certain user information in the background. The main difference, however, is that _cookies_ store this information **on the user's device** (mainly in the browser), while the _session_ is stored **on the server side**. Therefore, _session_ data is **not accessible** to third-party sites, as is the case with _cookies_ described in the previous paragraph. You may ask - so what's the problem then? Well, for the _session_ to work properly, it is necessary to store **one piece of data** on the user's computer, which is the _PHPSESSID_ (PHP Session ID), which is essential for linking the data stored on the server with a specific user. Theoretically, this ID can also be used by third-party sites to identify the user, but in this case, I wouldn't worry too much about it. The mentioned identifier ceases to exist in two cases:

- session termination by a script, which in our case are commands contained in the _logout.php_ file,

- closing the browser.

So it's hard to compare it to _cookies_, which can stay on our device for years and during that time store a lot of information that is not necessary for the proper functioning of the websites they relate to.

> TL;DR  
> _Session_ works similarly to _cookies_, but it only stores information necessary for the website to function properly on the user's side and ceases to exist after logging out or closing the browser. The advantage is that it takes care of the user's privacy, but the disadvantage is the need for more frequent logging in than in the case of a solution based on standard _cookies_.
