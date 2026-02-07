---
title: "Translator DeepL - translate using API [ENG 🇬🇧]"
date: 2023-03-01
categories: 
  - "tutorials"
tags: 
  - "api"
  - "curl"
  - "deepl"
  - "json"
  - "mastodon"
  - "opensource"
  - "php"
  - "translate"
  - "translator"
image: "/images/deeplapi.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/deepl-api/)

_DeepL_ is a machine translation service, which in simple terms can be described as a **translator**, operating based on neural networks. Interestingly, the CEO of the company behind this translator is a **Pole** - Jarosław Kutyłowski. I've been using _DeepL_ for almost 5 years now, instead of the widely known _Google Translate_, because it simply gives me better results, and also allows me to keep my data a little further from _Google_. For normal use, _DeepL_ is **free** and available from the website. You can also create an account and choose one of two access plans via _API_ - _Free_ and _Pro_. Of course, we are interested in the **free plan, which is limited to 500,000 characters per month**. For basic applications of a single user, this limit should be sufficient.

## How to get your API key

Let me keep it brief, so as not to dwell too much on such a simple process. We start, of course, with **creating an account** - [direct link to registration](https://www.deepl.com/pl/pro-checkout/account?productId=1200&yearly=false&trial=false). In the panel of your account, go to the _Account_ tab, and at the very bottom in the _API Identifying Key for DeepL_ section, you will find the _API token_, which we will need in the further part of this post. For more curious, I also recommend study the [API documentation](https://www.deepl.com/docs-api).

## Communication with DeepL API

The entire communication with the _DeepL API_ looks very similar to what I described in my post about the _[MEWS Bot = Mastodon nEWS](https://blog.tomaszdunia.pl/mews-eng/)_, where we used _cURL_ to communicate with the _Mastodon API_. The difference in this case is that with _DeepL_, we will not only send data (the text to be translated) but also expect a response (the translated text). As always, I have described the entire code step by step by placing comments in it. The script is available at the end of the post.

Before we dive into the script, I would like to discuss certain parts of it more broadly to provide perspective. One of the most crucial things in communication with an API via _cURL_ is properly constructed _**headers**_, which are a kind of a request preview that we will send to the server. In the case of the _DeepL API_, the only information that must be included in the header is the correct authentication data, i.e., presenting your _API_ key, based on which we obtain the right to communicate. The header should have the following form:

> Authorization: DeepL-Auth-Key \[API TOKEN/KEY\]

The second essential element of the _cURL_ request is the **_URL address_** to which the requests should be directed. In the case of _DeepL_, it is:

> https://api-free.deepl.com/v2/translate

The third element, without which the request would be meaningless, is the **actual data**, i.e., the request itself. It is best to send this data in the form of an _array_. We will send three things in it:

- string (text) to be translated,

- declaration of the language we want it to be translated into,

- declaration of the language in which the text we provided in point one is written.

The last point is not necessary, as _DeepL_ is able to recognize the language in which we have served the text to be translated. Nevertheless, from my experience using the web version of _DeepL_, I know that the language recognition algorithm is not infallible, so I definitely recommend clearly specifying this parameter for certainty.

OK, we send the properly constructed _cURL_ request to the _DeepL_ _API_, and what's next? We receive **feedback** in the form of a string in [_JSON_](https://en.wikipedia.org/wiki/JSON) (_JavaScript Object Notation_) format. We decode it using the _json\_decode()_ function. By the way, as the second argument when calling this function, we provide a value of _true_, which instructs the function to not only convert the _JSON_ string into a _PHP_ object, but also to convert that object into an array. In this way, we get the following result:

```php
Array
(
    [translations] => Array
        (
            [0] => Array
                (
                    [detected_source_language] => PL
                    [text] => Sample text in Polish that we want to translate into English
                )
        )
)
```

As we can see, we received a nested array, and the expected result is stored under the index _\[translations\]\[0\]\[text\]_. This way we have accessed the translated text we were looking for.

## PHP script code

As I mentioned earlier, below is the **entire code of the script** to which I referred to in this post. It is conventionally explained through **comments within the content**.

```php
<?php
// API key copied from DeepL profile
$token = "[Tu wpisz swój klucz API DeepL]";
// Example text in Polish that we want to translate to English
$tekstPL = "Przykładowy tekst w języku polskim, który chcemy przetłumaczyć na język angielski";

// Headers
$headers = [
    "Authorization: DeepL-Auth-Key ".$token
];
// Proper data
$data = array(
    "text" => $tekstPL, // Text to be translated
    "target_lang" => "EN", // Target language
    "source_lang" => "PL" // Source language
);

// Initializes cURL request
$translate = curl_init();
// Specifies the URL to which the request should be directed
curl_setopt($translate, CURLOPT_URL, "https://api-free.deepl.com/v2/translate");
// Declares that this is a POST request
curl_setopt($translate, CURLOPT_POST, 1);
// Instructs cURL to return the result of the request
curl_setopt($translate, CURLOPT_RETURNTRANSFER, true);
// Sets headers
curl_setopt($translate, CURLOPT_HTTPHEADER, $headers);
// Defines data to be passed
curl_setopt($translate, CURLOPT_POSTFIELDS, $data);
// Sends the request and saves the decoded result to a variable
$return = json_decode(curl_exec($translate), true);
// Closes the connection
curl_close ($translate);

// Extracts translated text from API response
$tekstENG = $return['translations'][0]['text'];

// Shows results
echo "<b>Tak wygląda zdekodowana odpowiedź z API DeepL:</b><br>";
echo "<pre>";
print_r($return);
echo "</pre>";
echo "<br><br><br>";

echo "<b>Tekst po polsku:</b><br>";
echo $tekstPL;
echo "<br><br>";
echo "<b>Tekst po angielsku (przetłumaczony przez DeepL):</b><br>";
echo $tekstENG;
?>
```

The result of the above script is as follows:

![](/images/AE24041A-B186-4F36-8C6C-75F53754948D.jpeg)

## BiLangPost

This post was written on the occasion of me releasing my next little project, which is [_BiLangPost_](https://bilangpost.tomaszdunia.pl). It is a **tool that facilitates writing bilingual posts** on social media, and it was specifically designed for _Mastodon_. Another tool project that I originally made for myself, but at some point, I came to the conclusion that I only need to change/add a few lines and I can make it available to a wider audience. In this post, I won't elaborate more because I will probably make a completely separate post only about _BiLangPost_.
