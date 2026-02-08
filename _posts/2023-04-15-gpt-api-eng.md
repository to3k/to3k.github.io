---
title: "Access to GPT by OpenAI via API [ENG 🇬🇧]"
date: 2023-04-15
categories: 
  - "tutorials"
tags: 
  - "ai"
  - "api"
  - "chatgpt"
  - "curl"
  - "deepl"
  - "futurepedia"
  - "gpt"
  - "gpt35turbo"
  - "gpt4"
  - "llm"
  - "max_tokens"
  - "openai"
  - "php"
  - "promptengineer"
  - "temperature"
  - "token"
  - "translate"
  - "translator"
image: "/images/openaiapi.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/gpt-api/)

Table of contents:
* TOC
{:toc}


_ChatGPT_ has been on everyone's lips lately. It seems like it's even coming out of our refrigerators. On the internet, TV, and radio, we constantly hear discussions about _whether it's the future_, _how many jobs it will take away_, _how innovative the solution is_. Well, I won't dwell on that too much and will focus only on practical aspects, because just like you, dear Reader, **I've had enough of empty talk**. I'll just say it briefly, **AI is undoubtedly the future**, whether we like it or not. Maybe not in its current form, but **it will evolve and develop very quickly**. The only thing we can do to actively participate in this future is to get on the fastest horse we have in the barn, ride ahead, catch up with that train, and try to **get on board while we still can**. For me, _GPT_ and other models like it are innovations of our time that can already be compared to the breakthrough that was smartphones, and this is just the beginning of the road. We are now facing a bigger challenge - **will you get on board or be left behind?!** I can't say that I'm already on the train called _AI EXPert EXPress_, because I feel like I've only just touched on the subject and only through a glass, but I'm riding on a horse and **I can take you on the back seat if you want and together we'll try to catch up with that train**. That's exactly what this post is about. Putting aside metaphorical babble - **in this post, I'll show you how to communicate with artificial intelligence created by _OpenAI_**, specifically using their _GPT_ model, through _API_ provided by them.

_OpenAI_ and their product have many opponents who express (in my opinion) valid doubts (greetings to MiKlo and Rysiek and I recommend checking out the comments under [my toot](https://mastodon.tomaszdunia.pl/@to3k/110187175119834883) announcing this post). I recommend that such people treat this post as a collection of information that will allow them to get to know their opponent, it always makes the fight easier 😉

## ChatGPT

When hearing about _OpenAI_, _GPT_, or _artificial intelligence_, most people think of _ChatGPT_. Indeed, it has greatly contributed to the popularization and discussion of _AI_ because it has demonstrated the power of this solution. _ChatGPT_ is a completely free tool (of course, there is a paid plan, but we're not talking about that here) that allows you to converse with _artificial intelligence_, or rather with a language model (_LLM_, short for _Large Language Model_), as if you were talking to a friend on _Signal_. However, we all need to understand that **_ChatGPT_ is not the end of the story and it is not the only form of access to machine learning models**, one of which is _GPT_, which is also short for _Generative Pre-trained Transformer_. This refers to an advanced machine learning model that has been trained on large sets of text data to generate coherent and logical sequences of natural language text. Why did I translate this as _transformer_? Because the simplest way to explain all of this is that **_GPT_ transforms messages understandable to the machine into messages understandable to humans and vice versa**. So, _ChatGPT_ can be treated as just one of the services based on _GPT_. Many other projects have already been created based on _GPT_, and new ones are created every day, as evidenced by the _[Futurepedia.io](https://www.futurepedia.io/)_ website. **Integrating the _GPT_ model into your project is possible through the _API_ provided by _OpenAI_**, and as it turns out, it's not difficult at all, as I will demonstrate in this post.

## How to Access the API

As with most _APIs_, to gain access to it we need to have a key. Such a key can be obtained by **registering on the website**: [https://auth0.openai.com/u/signup/identifier](https://auth0.openai.com/u/signup/identifier). Registration is free, and after that we get $5 to use for learning/playing. At first glance, these $5 may seem like a funny amount, but as soon as you see how much it costs to perform really complicated tasks, you will understand that **with these five dollars you can really move mountains**!

After creating an account, we enter the management panel of our account and then go to the _API Keys_ tab or you can simply use this link - [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys). Here, all we need to do is press the _+Create new secret key_ button and copy the key value that will be displayed in the window that pops up.

## Let's build a PL-ENG translator using the GPT model

You've probably used _Google Translate_ or even _DeepL_ to translate something before, as I wrote about in [this post](https://blog.tomaszdunia.pl/deepl-api/). However, **there's no way to compare how well the _GPT_ model handles translation compared to any of the previously mentioned tools**. As I write this post, I'm seriously considering translating most of the posts on this blog using _OpenAI's_ solution. By the time this is published, they may already be translated, although it depends on the final publication date I set for this post and the amount of time I have to check the generated translations, because let's not hide the fact that they need to be at least reviewed before publication.

But let's get back to the topic. Below, I present the code for a script that, using _cURL_ known to us from previous posts ([this one](https://blog.tomaszdunia.pl/mews/) and [this one](https://blog.tomaszdunia.pl/deepl-api/)), will communicate with the _OpenAI_ _API_ and send the user-provided text fragment for translation. The basic description of the individual steps of the script is located in the code as comments.

```php
<?php
    // OPENAI API TOKEN
    $token = '[TU_WKLEJ_TOKEN]';
    
    // Checks if the command and the text to be translated were sent
    if(!empty($_POST['polecenie']) AND !empty($_POST['fragment']))
    {
        // If yes, it retrieves the POST variable where it is stored
        $polecenie = $_POST['polecenie'];
        $fragment = $_POST['fragment'];
        
        // Specifies the maximum token limit we can declare
        // Specifies the length of the text fragment
        $prompt_size = strlen($polecenie) + strlen($fragment);
        // For the gpt-3.5-turbo model, the token limit is 4096, so we subtract the previously calculated length from this limit
        $max_tokens = 4096-$prompt_size;

        // Array with information sent in the cURL request
        $postfields = array(
            "model" => "gpt-3.5-turbo", // Określenie jaki model ma zostać użyty
            "messages" => [
                array(
                    "role" => "system", // Określenie roli wiadomości jako ta od systemu (nadająca kontekst)
                    "content" => $polecenie // Kontekst (w naszym przypadku polecenie, co ma być zrobione)
                ), 
                array(
                    "role" => "user", // Określenie roli wiadomości jako ta od użytkownika
                    "content" => $fragment // Fragment do tłumaczenia
                )
            ],
            "temperature" => 0.5, // Parametr, który określa jak kreatywna (losowa) ma być odpowiedź
            "max_tokens" => $max_tokens // Określenie jak długa może być odpowiedź
        );
        // Converts the above array into a JSON object, as it should be sent
        $postfields = json_encode($postfields);

        // Request headers
        $headers = array(
            "Content-Type: application/json", // Określenie typu wysyłanej treści - JSON
            "Authorization: Bearer ".$token // Token do uwierzytelnienia przy komunikacji z API
        );
        
        // Initializes the cURL request
        $curl = curl_init();
        // Specifies the URL to which the request should be directed
        curl_setopt($curl, CURLOPT_URL, "https://api.openai.com/v1/chat/completions");
        // Instructs cURL to return the query result
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        // Declares that this is a POST request
        curl_setopt($curl, CURLOPT_POST, 1);
        // Defines the data to be passed
        curl_setopt($curl, CURLOPT_POSTFIELDS, $postfields);
        // Sets headers
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
        // Sends the request and saves the decoded result to a variable
        $result = json_decode(curl_exec($curl), true);
        // Closes the connection
        curl_close ($curl);
        // Retrieves the translated text from the result
        $translated = $result['choices']['0']['message']['content'];
        // Retrieves the length of the query (tokens)
        $prompt_tokens = $result['usage']['prompt_tokens'];
        // Retrieves the length of the response (tokens)
        $completion_tokens = $result['usage']['completion_tokens'];
        // Retrieves the total number of used tokens from the result
        $total_tokens = $result['usage']['total_tokens'];
    }
    else
    {
        $polecenie = "Przetłumacz z polskiego na angielski";
    }
?>

<!-- HTML form -->
<form action="" method="POST" name="form">
    Polecenie (kontekst zadania):<br>
    <input name="polecenie" style="width: 100%;" value="<?php echo $polecenie; ?>"><br><br>
    <!-- Text field to enter the fragment to be translated -->
    Fragment do przetłumaczenia:<br>
    <textarea name="fragment" style="width: 100%; height: 35%;"><?php echo $fragment; ?></textarea>
    <br>
    <button type="submit">Tłumacz</button>
</form>

<?php
    // If there is a translation
    if(!empty($translated))
    {
?>

        <!-- Displays the translated text in a text field with editing disabled -->
        Przetłumaczony tekst:
        <textarea style="width: 100%; height: 35%;" disabled><?php echo $translated; ?></textarea>
        <br><br>

<?php
        // Calculates the cost of executing the task
        $cost = 0.002 * $total_tokens / 1000;
        // Displays the number of used tokens
        echo "Tokeny zapytania: ".$prompt_tokens." | Tokeny odpowiedzi: ".$completion_tokens." | Tokeny ogółem: ".$total_tokens."<br>";
        // Displays the cost of executing the task
        echo "Koszt (przy założeniu cennika dla modelu gpt-3.5-turbo = $0.002 / 1k tokenów): $".$cost;
        echo "<br><br><hr>";
        // Displays the API server response converted to an array
        echo "Odpowiedź serwera API:";
        echo "<pre>";
        print_r($result);
        echo "</pre>";
    }
?>
```

In this entire code, the three most important parameters of the cURL request are:

- _**CURLOPT\_URL**_ - the address to which the request is directed to the API,

- **CURLOPT\_HTTPHEADER** - the headers containing the _token_ used for authentication and access to the API,

- **CURLOPT\_POSTFIELDS** - the "meat," essence, and most important part, which is the information we send to the API.

I would like to focus only on this last parameter. It is transmitted in the form of a _JSON_ object with a strictly defined structure. I used the word "strict" because it is enough to make one mistake and the entire request will fail. In the script, I adopted the tactic of first creating an array, filling it with data, and only at the end converting it into a _JSON_ object. In any case, in this part of the cURL request, you can specify things such as:

- _**model**_ - the language model to be used (a list of all currently available models can be found [here](https://platform.openai.com/docs/models/overview)). At the time of writing this post, the latest model available without a subscription is _gpt-3.5-turbo_, while with a subscription ($20 per month), we have access to the _gpt-4_ model.

- **_message_** - divided into:
    - **_role_** - the following roles are available here:
        - _system_ - messages signed with this role are a very important tool for the user, available only through the API (using ChatGPT, it is not possible to use such a function). It is used to determine context, for example, we can write to _AI_ in what role it should appear - "you are a poet and you must respond in a thirteen-syllable verse", or simply use this function like I did in the above code to specify a specific task to be performed by _AI_ - "Translate from Polish to English",
        
        - _user_ - a role that indicates that the message comes from the user (from us),
        
        - _assistant_ - messages written by _AI_ are marked in this way,
    
    - **_content_** - the content of the message,

- **_temperature_** - temperature is used to define the level of creativity, or rather randomness in this case, as it's hard to say that a language model can be creative. We expect from _AI_ in response to a query. The closer the value is to 0, the more pragmatic the response will be (good when we expect a real answer to a question or simply ask it to perform a specific task), while the closer it is to 1, the more the model will simply start to invent (good when the task is creative, for example, the model has to come up with an advertising slogan).

- **_max\_tokens_** - the maximum length of the response measured in tokens, which unfortunately are difficult to convert to words or even letters. In practice, the smaller the _max\_tokens_ parameter, the more concise the response will be.

As you can see, by using this method, which is communication via an _API_, we do pay, but we have the possibility to configure a much larger number of parameters than in a normal conversation with _ChatGPT_. These parameters allow us to significantly determine our needs and optimize the process we create based on the use of _GPT_. In my opinion, it is particularly important to play with the _temperature_ parameter, which should be adjusted accordingly to the specific application. Nevertheless, it is also important to define the appropriate context by sending a message with a system role that outlines how _GPT_ should approach a given task. Formulating the right message is only the third important aspect of the entire process. People joke that new job positions will now be created called _Prompt Engineer/Specialist_. However, consider whether, after reading everything I wrote above, you also think that such specialization would make sense? If so, I suggest trying your own skills in squeezing from _GPT_, in an optimal way, exactly the answer you expect, good luck! 😉

## Let's check the script's performance

The result of the above script, after inserting the introduction of this post into it, looks like this:

![](/images/gptapi2.png)

As you can see, the quality of the translation is quite good. Of course, some corrections are needed, but it must be acknowledged that my style of expressing thoughts is not entirely easy to analyze, especially when it needs to be translated into another language. We used a total of 869 _tokens_ to complete this task, which translates to a cost of fractions of a cent (less than 0.2 cents, so in practice, you can complete five similar tasks for 1 cent, and you can do 500 of them for one dollar). Now you understand how much you can do with the five dollars I mentioned earlier?

## API Server Response

Finally, let's take a look at how the API server responds:

```markup
Array
(
    [id] => chatcmpl-74ECqgzzmsDLEH62Te6QXFxO72nqY
    [object] => chat.completion
    [created] => 1681242276
    [model] => gpt-3.5-turbo-0301
    [usage] => Array
        (
            [prompt_tokens] => 544
            [completion_tokens] => 325
            [total_tokens] => 869
        )

    [choices] => Array
        (
            [0] => Array
                (
                    [message] => Array
                        (
                            [role] => assistant
                            [content] => ChatGPT is currently on everyone's lips. It's almost coming out of our refrigerators. We hear discussions about it on the internet, TV, and radio all the time, such as whether it is the future, how many jobs it will take away, and how innovative the solution is. Well, I won't dwell on it too much here because, like you, dear reader, I'm a bit tired of all this talk for nothing. I'll just say briefly that AI is undoubtedly the future, whether we like it or not. Maybe not in its current form, but it will evolve and develop very quickly. The only thing we can do now is to get on the fastest horse we have in the corral, ride ahead, catch up with that train, and try to get on it while we still can. For me, GPT and other models like it are innovations of modern times that can already be compared to the breakthrough of smartphones, and this is just the beginning of the road. We are facing a challenge now - are you getting on board or falling behind? I can't say that I'm already on the train called the AI Expert Express because I feel like I've only just scratched the surface, but I'm on a horse, and if you want, I can take you on the back seat, and together we'll try to catch that train. That's exactly what this post is about. Leaving behind the metaphorical talk - in this post, I'll show you how to communicate with artificial intelligence created by OpenAI, specifically how to use the GPT model through their API.
                        )

                    [finish_reason] => stop
                    [index] => 0
                )

        )

)
```

As you can see, the response contains, among other things, the following information:

- the ID of the conversation, which raises the question of whether it is possible to refer to it later based on this ID... I haven't tested that yet,

- the model that was used,

- the number of tokens used, broken down into prompts, responses, and the total,

- the target response,

- the status of the response generation, where _stop_ indicates that the model completed the task correctly and stopped on its own, and e.g. _length_ indicates that the value of the _max\_tokens_ parameter was set too low, and the model simply did not have enough characters to complete the response correctly (in this case, it is usually just cut off where the available tokens ran out).
