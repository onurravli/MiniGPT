MiniGPT
=======

MiniGPT is a Python module that provides a simple interface for interacting with
OpenAI's GPT-3 API. With MiniGPT, you can easily create chatbots that can understand
natural language and respond accordingly.

**NOTE**: MiniGPT is not affiliated with OpenAI in any way. Also, you will need
an API key to use MiniGPT. You can **buy** one from the OpenAI website:
https://openai.com/

Installation
------------

To install MiniGPT, you first need to have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can install MiniGPT using pip:

`$ pip install minigpt`

Usage
-----

Here is an example of how to use MiniGPT:


.. code-block::

    from minigpt import MiniGPT

    mgpt = MiniGPT(key="YOUR_API_KEY")

    response = mgpt.chat(
        model="gpt-3.5-turbo",
        role="assistant",
        content="Hello, how can you help me?",
        temp=0.7
    )

    print(response)