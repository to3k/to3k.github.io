---
title: "BiLangPost - tool for publishing bilingual posts [ENG 🇬🇧]"
date: 2023-08-02
categories: 
  - "projects"
  - "tutorials"
tags: 
  - "api"
  - "bilangpost"
  - "bilingual"
  - "deepl"
  - "github"
  - "html"
  - "javascript"
  - "mastodon"
  - "php"
  - "post"
  - "toot"
  - "translate"
  - "translator"
image: "/images/bilangpost.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/bilangpost/)

[_BiLangPost_](https://bilangpost.tomaszdunia.pl/) is my next small and not very complicated project (you know how much I love such things 😉). It is a tool that facilitates writing bilingual posts. The reason for its creation is that when I joined _[Mastodon](https://mastodon.tomaszdunia.pl/@to3k)_, I decided to write in both Polish and English there. I am quite fluent in spoken and written English, but I am also a fan of automating everything that can be automated. With translations, it is always better to improve an imperfect translation than to write something twice (first in one language, then in the other). Considering the above, I thought it over, sat down at the code editor, and created the aforementioned tool using the _PHP_ language.

[![](/images/bc7ca2566e0eac59.png)](https://blog.tomaszdunia.pl/wp-content/uploads/2023/07/bc7ca2566e0eac59.png)

[![](/images/0b6c4ec5e220b563.png)](https://blog.tomaszdunia.pl/wp-content/uploads/2023/07/0b6c4ec5e220b563.png)

The operation principle is as follows: we write a message in the source language and indicate the target language. Then, BiLangPost translates the content from the source message to the target language and combines them, additionally formatting it to create a ready-to-publish post (or _toot_) on social media, for example. The underlying translation mechanism is powered by _[DeepL](https://www.deepl.com/translator)_, with which I communicate using _API_, as described in [this post](https://blog.tomaszdunia.pl/deepl-api-eng/). Speaking of the _DeepL API_, as you probably know from the linked article, it's free up to a certain limit. After exceeding that limit, a paid plan comes into play, which unfortunately is not among the cheapest. Consequently, I couldn't share my private _API token_ for use with this free tool, as my limit would be quickly exhausted, and the free package is sufficient for my personal needs. Therefore, anyone who wants to use _BiLangPost_ must use their own _API_ key. Of course, the key provided by the user is not stored or used by me in any other way than to perform the work of _BiLangPost_ assigned to it in a given session.

## Let's Take a Look at the Code

The entire code is, of course, open and [available for review on GitHub](https://github.com/to3k/bilangpost). The substantive part related to the translation, i.e., how to properly communicate with the _DeepL API_, was already described on the blog, so I won't repeat that here. However, there is one thing in the _BiLangPost_ code that I'd like to discuss. It's a mechanism I created so that users wouldn't have to manually enter their _API token_ and select translation languages each time, without using cookies and/or sessions. I came up with a solution where I take a variable that stores the user's provided _API token_ and variables that specify the chosen source and target languages, then I combine them into one variable separated by semicolons. Next, I encrypt the value of this variable using the _openssl\_encrypt()_ function and store it as a global variable of type _$\_GET_ (the one stored in the _URL_). This way, the user can use this special URL on their next visit, containing the embedded variable with the necessary information, without having to configure everything from scratch. It's a solution that is both convenient and relatively secure because the user's API token is not exposed as plaintext in the URL.

The previously mentioned _openssl\_encrypt()_ function has three main parameters:

1. _$data_ - the data to be encrypted,

3. _$cipher\_algo_ - declaration of the encryption algorithm to be used (I chose _AES-128-CTR_),

5. _$passphrase_ - encryption key, without which decryption is not possible.

The encrypted value can be decrypted using the complementary _openssl\_decrypt()_ function, which takes analogous parameters.

```php
<?php
    // Variables necessary for encryption process
    $passphrase = "[encryption key for encrypting GET variable with settings]";
    $cipher_algo = "AES-128-CTR";
    // Declaration of a variable to store settings
    $settings = "";
    [...]
?>

<!-- HTML Form -->
<form action="/?set=<?php echo $set; ?>" method="post">
    [...]
    <button type="submit" name="PreparePost" value="PreparePost">Prepare post!</button>
</form>

<?php
    [...]
    // If HTML form has been submitted
    if(isset($_POST['PreparePost']))
    {
        // Encryption process
        $settings = $token.";".$lang1.";".$lang2;
        $set = openssl_encrypt($settings, $cipher_algo, $passphrase);
    }
    [...]
    // If global variable (GET) set is not empty
    if(!empty($_GET['set']))
    {
        // Decryption process
        $set = addslashes(strip_tags($_GET['set']));
        $decrypted_set = openssl_decrypt($set, $cipher_algo, $passphrase);
        $explode = explode(";", $decrypted_set);
        $token = $explode[0];
        $lang1 = $explode[1];
        $lang2 = $explode[2];
    }
    [...]
?>
```

## Text Area Handling

Front-end has never been my strong suit, and it's a bit embarrassing to admit, but I am completely unfamiliar with the _Javascript_ language. In the realm of _HTML_, _PHP_, or even _MySQL_, I navigate without much difficulty, but _JS_ has always been a big question mark for me. Somehow, I never had the time to sit down and familiarize myself with it. It's often a significant problem for me because it's undeniable that 99% of the Internet is built on _Javascript_. Whenever I need to implement something written in _JS_ on one of my pages, I simply search for similar ready-made solutions that I modify to suit my needs. The same was for _BiLangPost_, where I needed to learn how to handle text areas, specifically to accomplish three things:

1. to dynamically expand the text area when the entered text no longer fits within it,

3. to count the number of characters entered in the text area so that the user can see in real-time if they are within the character limit they set for themselves,

5. to add a button that allows one-click copying of the entire content of the text area.

The base HTML code for modification:

```markup
<textarea
    id="textarea"
    name="message"
    placeholder="Write here in your native language..."
>[Content]</textarea>

<button type="button" name="CopyButton">Copy</button>
```

To handle the issue of a self-scaling area (resizing beyond the default size), you can do it quite easily by adding a parameter to the _<textarea>_ element.

```markup
<textarea [...] oninput='this.style.height = "";this.style.height = this.scrollHeight + "px"'></textarea>
```

If I understand the notation correctly, it simply means that the height parameter of the text area is dynamically updated while entering successive characters into the area, overwritten with a value equal to the scrollbar's height.

For counting the number of characters inside the area, I created a function that initializes a variable called _counter_, in which the current length of the string entered inside the designated text area is saved. Calling this function occurs through an event named _onKeyUp_, which, in simple words, means "when a keyboard button is released." This event occurs when we press a key on the keyboard and release it (precisely at the moment of release). Finally, we need to display the calculated value below the text area.

```markup
<textarea onKeyUp="count_it()" [...]></textarea>

<div>Characters: <span id="counter"></span></div>

<script>
    function count_it()
    {
        document.getElementById('counter').innerHTML = document.getElementById('textarea').value.length;
    }
    count_it();
</script>
```

Finally, we have a button left for copying the content of the text area with a single click. The script handling this functionality consists of a function where we first define the specific text area by its identifier (_Id_). Then, the content of the area is selected, and with the next command, the selected content is copied to the user's clipboard. At the end of the function, there is an additional bonus in the form of changing the text inside the button (label) after it is clicked. The text _Copy_ changes to _Copied!_. After finishing the script, remember to add the _id_ and _onclick_ parameters to the button. The latter informs the interpreter about what should happen when the button is clicked, in this case, the _copy()_ function we previously wrote should be called.

```markup
<button [...] id="CopyButton" onclick="copy()">Copy</button>

<script>
    function copy()
    {
        let textarea = document.getElementById("textarea");
        textarea.select();
        document.execCommand("copy");
        var btn = document.getElementById("CopyButton");
        btn.innerHTML = "Copied!";
    }
</script>
```

## BiLangPost is waiting to serve

At the end of this post, I just wanted to invite you once again to the dedicated website of the _BiPangPost_ tool!  
\> [https://bilangpost.tomaszdunia.pl](https://bilangpost.tomaszdunia.pl) <  
A sample toot written using _BiLangPost_ looks like this:

<iframe src="https://mstdn.social/@to3k/109930509908621693/embed" width="100%" height="300px" allowfullscreen="allowfullscreen" sandbox="allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox allow-forms"></iframe>
