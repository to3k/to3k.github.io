---
layout: post
title: "OpenClaw + OpenRouter [ENG 🇬🇧]"
published: true
categories: 
  - "projects"
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "openrouter"
  - "openclaw"
  - "hetzner"
  - "ai"
  - "llm"
  - "bot"
  - "assistant"
  - "gemini"
  - "chatgpt"
  - "claude"
  - "openai"
  - "anthropic"
  - "google"
  - "vps"
  - "ssh"
  - "telegram"
  - "api"
image: "/images/openrouter.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/openrouter/)

Table of contents:
* TOC
{:toc}

## Introduction

This post is a continuation of - **[OpenClaw - Personal AI Assistant](https://blog.tomaszdunia.pl/openclaw/)**, where I described how to start your journey with **OpenClaw**. As a reminder, I used the **free Gemini API** under the **Free Tier** in **Google AI Studio** for testing. In the conclusions of that previous post, I realized that while this model is sufficient to check the general concept and see if OpenClaw works at all, it was clearly the **weakest point of the environment** and needed to be modified. That modification is **connecting a paid API** of one of the leading current models. Many people online recommend using OpenClaw with **Claude Sonnet** from **Anthropic**. Others say it's too expensive and better to go with the slightly cheaper **Gemini 3 Pro** from **Google**. There are also other camps suggesting the **superiority of more niche models due to their price-to-quality ratio**. I see the following problems here:
1. **Each model is specialized in something else**; model A might be better at coding, while model B is better at generating images.
2. **There is no single leader**; although one of the well-known models often comes out in a new version and pulls ahead of the rest, others catch up shortly after, and the chase continues—only the rabbit changes.
3. **Overpaying for simple tasks**—you don't always need a high-end model. Paying for Claude Opus tokens assigned to check the weather today and determine if you need an umbrella is like hiring a lawyer to bring mail from your mailbox to your door, or using a sledgehammer to crack a nut.

Do you see what I mean? **There is no single solution (model) optimized for both performance and cost at the same time.** It's impossible to decide on just one model because if we go with something more advanced, we'll pay dearly for it, and if we optimize for costs, we won't be satisfied with the results of a "clunky" cheap model. If only there were a way to have your cake and eat it too—meaning, to have one tool that brings together many models within its service, allowing you to seamlessly switch between them depending on your current needs... 🤔

And this is where **[OpenRouter](https://openrouter.ai/)** enters on a white horse. Contrary to what you might think, this material is NOT sponsored! :)

## What is OpenRouter

**OpenRouter** is a **centralized platform** acting as a universal interface (API) for **almost all AI language models available on the market**. **Instead of setting up separate developer accounts** with providers like OpenAI, Google, Anthropic, or Mistral, you register in only one place and generate **one universal access key**. This allows you to **freely switch between flagship engines**—such as GPT-4o, Claude 3.7 Sonnet, or Gemini Pro—by simply swapping the model ID in the configuration of your application or assistant.

Billing on the platform works on a convenient **prepaid model** with a shared wallet. You pay a single deposit (e.g., $10), and the system deducts fractions of a cent for actually consumed tokens, **regardless of which company's services you are currently using**. Crucially, this solution has no hidden financial catches. **Token prices are exactly the same as when purchasing access directly from their creators**, because the platform earns from its own wholesale B2B discounts, not on margins for end users.

Another powerful advantage of this solution is reliability and freedom from territorial barriers. OpenRouter gives instant access to the latest models, which are often **initially blocked for users in Europe due to legal regulations**. The platform's unified API also fits perfectly into the configuration of fallback model chains. If a main provider's servers fail or impose a Rate Limit, the system can redirect your command to a backup engine from another company in a fraction of a second and **without interrupting your work**.

## Registration

1. Go to **[https://openrouter.ai/](https://openrouter.ai/)** and click the **Sign Up** button in the top right corner.
2. Enter your login and password and accept the terms of service. Confirm with the **Continue** button.
3. Check your email client and confirm your email.
4. After successfully logging in, find the three horizontal lines icon in the top right corner. Hovering over it will expand a menu from which you select **Settings**. From the menu on the right, choose **Settings -> Account**, then in the **User** row, click **Manage**. Go to the **Security** tab and in the **Two-step verification** row, click **+ Add two-step verification**. I recommend using this additional security layer before depositing any money. As always, I recommend the **[Ente Auth](https://github.com/ente-io/ente)** app.

## Topping up the account

1. Return to **Settings** and this time go to **[Credits](https://openrouter.ai/settings/credits)**. This is where you will manage your finances.
2. In the **Buy Credits** section, click the purple **Add Credits** button.
3. A window will appear where you enter your `name and surname`, `country`, and `address`. Confirm with **Update Address**.
4. In the `Add a Payment Method` window, start by checking **Use one-time payment methods** at the bottom.
5. The window will change to `Purchase Credits`. This way, instead of adding a permanent payment method, you will only make a one-time purchase of credits. This is a much safer solution because it removes the possibility of draining your debit card or getting into debt on your credit card.
6. Start the purchase by entering the amount you want to buy in the **Amount** field. This value cannot be less than 5 (or greater than 25000...). I decided to deposit $10. A tax of $0.80 will be added to this.
7. Now you can choose the **payment method**. You can choose from:
    - Card,
    - Fast bank transfer (although I couldn't find my bank),
    - WeChat Pay,
    - Alipay,
    - Cash App,
    - Cryptocurrencies,
    - Link,
    - Amazon Pay.
8. I chose **card** and entered my virtual Revolut card details. This way, I am not only protected by doing a one-time transaction, but the virtual card is also prepaid, meaning it only has as much money as I deposit onto it beforehand.
9. The $10 amount was immediately added to my account.

## Bot Optimization

Before we connect OpenRouter to our OpenClaw agent, we should optimize it a bit. Now that **real money** is involved, if you **don't want to pay for nonsense**, you need to change the bot's settings to minimize those mistakes.

### Editing personality files

In the [OpenClaw guide](https://blog.tomaszdunia.pl/openclaw/#podpowied%C5%BA), I wrote that it's good practice to **keep it to a minimum** regarding the files defining the bot's "personality." These files are **included in every request** sent to the API, so **the more extensive they are, the more we pay**. Therefore, let's look at them and make some changes. We can modify them in two ways:
1. From the terminal on the VPS by going to the folder where they are located `cd /home/manager/.openclaw/workspace` and editing them one by one using the `nano` editor.
2. From the control panel by going to **Agent -> Agents -> Files**.

Let's go through them one by one.

#### AGENTS.md

I'm not changing the content of this file and leaving it as default. I might introduce some changes in the future, but for now, I don't see the need. In my opinion, this is the most important file, providing general instructions for the bot's behavior and how to use the other files listed below. Be careful when editing it, as you might unintentionally "impair" the bot.

#### SOUL.md

As a reminder, this file defines how the bot should behave. The content of my `SOUL.md` file is:

```
- Direct, technical assistant.
- Respond as concisely as possible, without unnecessary fluff or greetings.
- Avoid corporate jargon and artificial politeness.
- If you are not sure about something, say "I don't know" directly instead of making things up or hallucinating.
```

#### TOOLS.md

I suggest leaving this file in its original form.

#### IDENTITY.md

The file where we create the bot's identity:

```
- Nickname: Areczek
- My personal AI assistant.
- Running in Docker on a Hetzner VPS.
- Communication: Telegram.
```

#### USER.md

Here we put basic information about ourselves that we consider useful for collaborating with the bot:

```
- Name: Tomasz
- Job: Engineer, designer, mechatronics, city bus industry.
- Hobbies: technical blog (blog.tomaszdunia.pl), self-hosting, smart home (Home Assistant), open source, sport shooting (firearms).
- Sports: Motorsports (speedway, F1).
- Socials: Mastodon - infosec.exchange/@to3k
- Location: Lublin, Poland.
```

#### HEARTBEAT.md

Clear it to zero. This is where recurring and background tasks will go, but the bot will fill this in itself. You can check here occasionally to see if it's performing any strange tasks in the background (without your knowledge).

#### BOOTSTRAP.md

This file is only useful during the bot's first run. The configuration we are doing now replaces this first step, so we clear this file so it doesn't unnecessarily clutter our prompts.

#### MEMORY.md

In my case, this file didn't exist by default, so I created it and left it empty. This is the place where the bot itself will save things it needs to keep in long-term memory.

#### Pro Tip

The above files are used to customize the assistant to your needs. As they say, appetite comes with eating, so we will definitely want to tweak something in the future. Our requirements for the assistant will also change. A good employee can always be better. Modify these files until you achieve a satisfying result. However, remember one thing. Some LLMs cache the content of these files. An example of such a model is Claude from Anthropic. After the first reading of our assistant's "personality" files, this model will remember them, and for the next API request, we will pay only 90% for using this part of the memory. There is one condition: the content of these files must not change. Any even minor change will cause re-caching, and thus we lose the 90% discount.

### Disabling unnecessary skills

OpenClaw starts with default skills, which in my case was as many as 50. I reviewed the entire list and concluded that I don't need any of them, and even if I do in the future, I can quickly enable them. The instructions for all enabled skills are attached to every request sent to the API, so if we don't use them, they are just unnecessary filler. You can check the list of skills in the control panel under **Agent -> Skills**, and you can also disable them all from there. Clicking `Disable` 50 times isn't convenient, so I suggest doing it from the VPS terminal. To do this, edit the file `/home/manager/.openclaw/openclaw.json`.

```bash
nano /home/manager/.openclaw/openclaw.json
```

Skills are located in the `skills` section and then `entries`, and they are disabled by changing the value of the `enabled` parameter to `false`. Example of disabling the 1password skill:

```json
"skills": {
  "entries": {
    "1password": {
      "enabled": false
    },
    ...
  }
```

### Limiting short-term memory

Every subsequent message we send generates another prompt call to the API (for which we pay). Each such subsequent **prompt contains the history of the given chat**, i.e., a number of messages from the Telegram conversation looking back. You could loosely call this the **bot's short-term memory**. Obviously, **the larger the block of text with history** sent in each prompt, **the more tokens are consumed** and **the more we pay**. Therefore, we will set a much **lower limit** here than, say, the Claude Sonnet model allows, for which the `Context Limit` can be up to 200,000. Let's set the value of this parameter **4 times lower**, i.e., 50,000.

If you're worried that this will essentially make the assistant "stupid," don't worry, because **OpenClaw has the `MEMORY.md` file**, which is like **long-term memory**. Reducing the capacity of short-term memory will only mean that the bot will **more frequently make summaries and save what's important in a shortened version to the file** with long-term memory.

This parameter is defined in the file `/home/manager/.openclaw/openclaw.json`, so let's open it for editing:

```bash
nano /home/manager/.openclaw/openclaw.json
```

In its content, we need to find `agents`, then `defaults`, and finally add `"contextTokens": 50000`. Below I'm providing a fragment of the `openclaw.json` content to show how to add it:

```json
"agents": {
    "defaults": {
      "model": {
        ...
      },
      "models": {
        ...
      },
      "compaction": {
        ...
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      },
      "contextTokens": 50000
    }
  },
```

Of course, save and close the file - **Control (CTRL) + X**, then **y** and **ENTER**.

### Restarting the container

Finally, let's restart the container to load the new configuration with all the changes described above:

```bash
docker compose restart openclaw-gateway
```

I think our bot is now worthy of having money loaded into it.

## Universal API Key

We return to the [OpenRouter](https://openrouter.ai/) website and finally obtain that legendary universal API key, giving access to a database of so many different models from various providers.

1. Go to **Settings -> [API Keys](https://openrouter.ai/settings/keys)** and click the purple **Create** button.
2. In the window that appears:
    - In the `Name` field, provide a name for our key, e.g., **OpenClaw Assistant**.
    - In the `Credit limit (optional)` field, we can enter a credit limit we want to impose on this key; I entered **5 dollars**. If left empty, it's unlimited (who's going to stop the rich...).
    - The `Reset limit every...` dropdown connects directly to the previous limit field and defines the limit reset interval; I chose **Daily**, because I can handle the bot eating up $5 in one day.
    - The `Expiration` dropdown allows us to define the lifespan of this API key; I chose **No expiration** because I have no problem with the key being eternal since it will be useless once the entire balance is used—and remember, I chose the prepaid billing model instead of adding a card permanently.
3. Confirm with the **Create** button.
4. As a result, we will receive a message containing the key, which should be saved in a safe place:

    ```
    Your new key:
    OPENROUTER_API_KEY_HERE

    Please copy it now and write it down somewhere safe. You will not be able to see it again.
    You can use it with OpenAI-compatible apps, or your own code
    ```
5. We will now add the received key to our bot's environment. Open the file `/home/manager/openclaw/.env` for editing:

    ```bash
    nano /home/manager/openclaw/.env
    ```
6. Add a line at the end, where instead of `OPENROUTER_API_KEY_HERE` you provide the OpenRouter API key created in the previous steps:

    ```bash
    OPENROUTER_API_KEY=OPENROUTER_API_KEY_HERE
    ```
7. Open another file for editing: `/home/manager/openclaw/docker-compose.yml`:

    ```bash
    nano /home/manager/openclaw/docker-compose.yml
    ```
8. At the end of the `environment` section, add the line:

    ```bash
    - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
    ```
9. One last container restart:

    ```bash
    docker compose up -d openclaw-gateway
    ```

## Multi-Model Strategy

OpenRouter is an excellent service. It's brilliant in its simplicity. It doesn't rob its users with any additional margins, and thus has a simple earning model based on bringing together many retailers, offering them the same prices as individual producers, and earning from the fact that it actually buys in bulk—because many retailers combined are essentially a wholesaler—and thus gets better prices, which implies income based on the difference between wholesale and retail prices.

However, for us, besides the prices, the most important function offered by OpenRouter is the ability to juggle—i.e., seamlessly jump between individual models. Of course, you could decide on one model, e.g., Claude Sonnet, link it permanently with your OpenClaw bot, and eventually replace it in the future with some other model that comes out and proves to be more efficient. But it would be a sin not to go deeper and take advantage of the flexibility OpenRouter offers. This is where the Multi-Model strategy comes in.

There are many ways to approach using multiple models, but I will present only the simplest one that requires the least attention. Let's call it the "solution for the lazy."

### Auto Router

Whoever is behind OpenRouter has a good head on their shoulders. They came up with a mechanism that works like this:
1. We send a request to OpenRouter using the API key.
2. The request goes to a small, ultra-fast meta-model run by OpenRouter, which we'll call the "gatekeeper."
3. In a fraction of a second, the gatekeeper performs a basic analysis of our request for intent classification:
    - **Complexity Scoring** - The gatekeeper scans the prompt for difficulty. If it detects a task requiring advanced reasoning (e.g., writing code, architectural analysis, math), it gives it a high weight and directs it to frontier-class models (like Claude 3.7 Sonnet or GPT-4o). If it's a trivial task (e.g., routine bot heartbeat, translation, simple classification), it directs it to cheap models (like Llama 3 or Gemini Flash).
    - **Context Windowing** - The system counts tokens on the fly (length of the message and pasted logs or chat history). If you send a data packet of 50,000 tokens, the router automatically rejects models that have a smaller memory window and selects the one that can physically handle that request volume.
    - **Live Telemetry (Health & Latency Check)** - OpenRouter constantly monitors the status of provider servers. The routing decision takes into account whether the Anthropic or OpenAI API is having a hiccup (Rate Limits) at that moment. If the main, intelligent model from one provider doesn't respond, the router dynamically shifts the request to its counterpart at another company.
4. After classification, the **Proxy and Forwarding** step occurs—after making a decision, the algorithm overwrites the target model ID in the HTTP headers and sends the request through its unified API to the selected creator's servers. The result comes back to you through the exact same channel.

Sounds promising, right? It convinced me, which is why I first decided to test this variant and am doing so right now. I'll probably update this post later with my thoughts after testing.

Okay, but how to configure it?
1. Log in to the VPS server:

    ```bash
    ssh manager@IPV4_ADDRESS
    ```

2. Open the file `/home/manager/.openclaw/openclaw.json` in the editor:

    ```bash
    nano /home/manager/.openclaw/openclaw.json
    ```

3. Modify its content to look as follows:

    ```json
    {
      "meta": {
        "lastTouchedVersion": "2026.2.20",
        "lastTouchedAt": "2026-02-24T22:48:06.665Z"
      },
      "agents": {
        "defaults": {
          "model": {
            "primary": "openrouter/openrouter/auto"
          },
          "heartbeat": {
            "every": "6h",
            "model": "openrouter/google/gemini-3-flash",
            "target": "last"
          },
          "compaction": {
            "mode": "safeguard"
          },
          "maxConcurrent": 4,
          "subagents": {
            "maxConcurrent": 8
          },
          "contextTokens": 50000
        }
      },
      "messages": {
        "ackReactionScope": "group-mentions"
      },
      "commands": {
        "native": "auto",
        "nativeSkills": "auto",
        "restart": true
      },
      "channels": {
        "telegram": {
          "enabled": true,
          "dmPolicy": "pairing",
          "botToken": "TELEGRAM_TOKEN",
          "groupPolicy": "allowlist",
          "streamMode": "partial"
        }
      },
      "skills": {
        "entries": {
          "1password": {
            "enabled": false
          },
          ...
          "weather": {
            "enabled": false
          }
        }
      },
      "plugins": {
        "entries": {
          "telegram": {
            "enabled": true
          }
        }
      }
    }
    ```

4. Let's discuss this file line by line:
    - **`meta`**: Configuration file metadata.
      - **`lastTouchedVersion`**: The version of the OpenClaw system that last overwrote or updated this file (2026.2.20).
      - **`lastTouchedAt`**: Exact date and time of the last modification.
    - **`agents.defaults`**: Default settings for your assistant.
      - **`model`**: The bot's main "brain." Assigning `auto` from OpenRouter means the system itself selects the optimal model for each request.
      - **`heartbeat`**: Proactive background operation configuration.
        - **`every`**: Time interval (waking up every 6 hours).
        - **`model`**: Engine dedicated to this task (set to the fast and cheap Gemini 3 Flash).
        - **`target`**: Specifies who the bot should direct any messages generated in the background to (`last` means the last used channel/last interlocutor).
      - **`compaction.mode`**: Short-term memory management mechanism. The `safeguard` mode compresses and summarizes the oldest chat messages, preventing token limit exhaustion.
      - **`maxConcurrent`**: Maximum number of operations (e.g., simultaneous use of several tools) that the main agent can perform in parallel (4).
      - **`subagents.maxConcurrent`**: Maximum number of independent background sub-workers the agent can launch to help with complex tasks (8).
      - **`contextTokens`**: Hard limit on chat memory (50,000 tokens) sent to the API with each message.
    - **`messages`**:
      - **`ackReactionScope`**: Defines situations in which the bot should confirm reading a message with a reaction (e.g., emoji). The value `group-mentions` means it will do this only when directly mentioned (@) in a group chat.
    - **`commands`**: Configuration for handling commands entered in the chat (e.g., on Telegram using a slash `/`).
      - **`native`**: Automatically enables and handles basic system commands (e.g., `/model`).
      - **`nativeSkills`**: Automatically registers and handles commands coming from installed skills.
      - **`restart`**: Allows using the `/restart` command directly from the communicator to reset the process.
    - **`channels.telegram`**: Telegram interface configuration.
      - **`enabled`**: Activates communication through this channel.
      - **`dmPolicy`**: Rules for private messages. The `pairing` mode means every new user must provide an authorization code for the bot to talk to them.
      - **`botToken`**: Your authentication password from BotFather.
      - **`groupPolicy`**: Rules for groups. The `allowlist` mode blocks the bot from acting in unknown group chats unless you add them to the whitelist beforehand.
      - **`streamMode`**: Text streaming mode. The value `partial` makes long responses update in Telegram in batches, mimicking smooth "live typing" without spamming the communicator API with every single word.
    - **`skills.entries`**: Place where manually installed additional skills from ClawHub are saved (currently empty).
    - **`plugins.entries.telegram.enabled`**: Enables the native module (engine plugin) responsible for maintaining the connection with Telegram servers.
5. As you can see, I linked `openrouter/openrouter/auto` as the main model, but additionally for `heartbeat` (background cyclic operations), I permanently assigned the `openrouter/google/gemini-3-flash` model—the fastest and cheapest model from the newest Gemini version. Theoretically, Auto Router would handle selecting the appropriate model for heartbeats, but configuring it permanently is so simple that it's worth avoiding any risk. Also, this allows me to strictly define the interval for background actions, and I decided on 6 hours to start.
6. Now let's reset the container to save the changes:

    ```bash
    docker compose restart openclaw-gateway
    ```

And how does it work in practice? Quite simply. I noticed that the entire dialogue with me on Telegram is conducted based on the Gemini 2.5 Flash model. If the agent gets a harder task, it delegates it to a subagent, which performs it on a more complex model. In my case, Claude Opus was selected, for which I unfortunately paid quite a bit, as it is one of the most expensive among the available models. I must admit, however, that I assigned the agent a rather complex task for which the instruction itself was a quite long prompt. I think I need to learn a bit more about optimization, because I'll go bankrupt pretty quickly this way.

## OpenRouter beyond OpenClaw

OpenRouter can also be **used like a regular chat**. Just go to the **[https://openrouter.ai/chat](https://openrouter.ai/chat)** website. However, it's not exactly a normal chat. Since OpenRouter is an LLM model aggregator, we can not only jump seamlessly between models and ask them subsequent questions alternately, but we can also ask the same question to several models at once or enable the Auto Router function, which will match the appropriate model itself to optimize costs and result quality.

I also recommend checking out the **[Model Rankings](https://openrouter.ai/rankings)**, which is an invaluable source of information on which models are currently trending (most frequently used). This way, you can pick up which model is currently the most effective, but also which one is the most cost-effective due to its quality-to-price ratio.

Meanwhile, the **[Model Database](https://openrouter.ai/models)** offers very extensive and detailed search filters, helping to find a model suitable for a specific application.
