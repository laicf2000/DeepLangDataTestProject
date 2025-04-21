import gradio as gr
import traceback


def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"



def extract_p_text(html_content):
    result = []
    start_tag = "<p>"
    end_tag = "</p>"
    index = 0
    while index < len(html_content):
        start_index = html_content.find(start_tag, index)
        if start_index == -1:
            break
        start_index += len(start_tag)
        end_index = html_content.find(end_tag, start_index)
        if end_index == -1:
            break
        p_text = html_content[start_index:end_index]
        result.append(p_text)
        index = end_index + len(end_tag)
    return "\n".join(result), "SUCCESS"

def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("HTML 文本处理"):
            html_input = gr.Textbox(lines=5, placeholder="输入 HTML 文本", label="输入 HTML 文本")
            p_text_output = gr.Textbox(label="提取的 <p> 标签文本")
            status_output_html = gr.Textbox(label="状态信息")

            btn_html = gr.Button("提取 <p> 标签文本")
            btn_html.click(
                fn=extract_p_text,
                inputs=html_input,
                outputs=[p_text_output, status_output_html],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )


if __name__ == "__main__":
    main()
