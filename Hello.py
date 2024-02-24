import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="st.write and magic",
        page_icon="👋",
    )

    st.write("# st.write and magicコマンド 👋")

    st.sidebar.success("上記「サブメニュー」を選択")

    st.markdown(
        """
        streamlitはあなたのアプリに情報を表示する2つの簡単な方法があり、通常はまずここから始めましょう。
        st.writeとmagicです。
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
