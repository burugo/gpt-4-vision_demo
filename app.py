import streamlit as st
import openai
import time
import base64

# 设置 API 密钥
api_key = '请输入 API 密钥'

# 初始化 OpenAI 客户端
openai.api_key = api_key

st.title("GPT-4-vision 示例机器人")

# 输入提示
prompt = st.text_input("请输入提示:")

# 上传图片
image_file = st.file_uploader("上传图片", type=["jpg", "png", "jpeg"])

if image_file:
    # 将上传的图片转换为二进制格式
    image_data = image_file.read()
    # 使用 Base64 编码
    image_base64 = base64.b64encode(image_data).decode()
    
    # 显示缩略图
    st.image(image_data, caption="上传的图片", use_column_width=True)


if st.button("生成") and image_file:
    while True:
        try:
            # 开始计时
            start_time = time.time()

            # 发送文本生成请求
            response = openai.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": image_base64},  # 将图片数据作为二进制格式传递
                ],
                max_tokens=2000,
            )

            # 结束计时
            end_time = time.time()

            # 执行时间
            execution_time_ms = (end_time - start_time) * 1000
            st.write(f"执行时间(ms): {execution_time_ms}ms")

            # 获取生成的文本
            generated_text = response.choices[0].message.content
            st.write("回答:\n" + generated_text)
            break

        except openai.OpenAIError as e:
            # OpenAI API 的一般错误
            st.write(f"OpenAI API 错误")
            st.write(e)
            break
        except Exception as e:
            # 其他错误
            st.write(f"错误")
            st.write(e)
            break
