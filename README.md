# gpt-4-vision_demo
vision_demo with streamlit
![image](https://github.com/tkys/gpt-4-vision_demo/assets/24400946/8a54c84b-23cf-4b55-b90b-e78ce5172cb8)


## install
```
$ pip install -r requirements.txt
```


## api  key
OpenAIから自身アカウントのAPI Keyを取得して利用してください
```
api_key = 'APIキーをここに入力'
```
## 起動
```
$ streamlit run app.py
```
[http://localhost:8501/](http://localhost:8501/)へブラウザからアクセス



- responseの抜粋
```
response:
ChatCompletion(
  id='chatcmpl-8I8hQ9EUOXCUPrfF5p6YHGii6OnHD',
  choices=[
    Choice(
    finish_reason=None,
    index=0,message=ChatCompletionMessage(
      content='ウィキペディアのロゴ画像です。ウィキペディアはインターネット上の無料百科事典です。多数のボランティアによって編集され、様々な言語で情報が集められています。',
      role='assistant',
      function_call=None,
      tool_calls=None
    ),
    finish_details={'type': 'stop', 'stop': '<|fim_suffix|>'})
  ],
  created=1699334036,
  model='gpt-4-1106-vision-preview',
  object='chat.completion',
  system_fingerprint=None,
  usage=CompletionUsage(completion_tokens=81, prompt_tokens=50, total_tokens=131)
)

```
##
2023-11-07 時点では `gpt-4-vision-preview` はまだ `preview`なのですぐに Rate Limitになりがち
