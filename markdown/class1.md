# Streamlit 程式技巧筆記

## 1. `import streamlit as st`

這行代碼導入了 Streamlit 庫，並使用 `st` 作為縮寫來引用它。

## 2. `st.title("這是標題")`

用來顯示應用程式的標題。

```python
st.title("這是標題")
```

## 3. `st.write()`

用來顯示多種格式的內容，包括字串、數字、Markdown、數據框等。

```python
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
```

## 4. `st.text()`

用來顯示純文字字串，只能顯示純文字，不支持其他格式。

```python
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
```

## 5. `st.markdown()`

用來顯示支持 Markdown 語法的字串，可以處理 Markdown 格式的內容。

```python
    st.markdown(
        '''
    這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
    例如：
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 代碼塊：
    ```python
    print("Hello, Streamlit!")
    ```

    '''
    )

```

### 示例代碼

```python
    import streamlit as st

    st.title("這是標題")
    st.write(
        "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
    )
    st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
    st.markdown(
        '''
    這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
    例如：
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 代碼塊：
    ```python
    print("Hello, Streamlit!")
    ```

    '''
    )

```

### 使用技巧總結

- `st.title` 用於顯示標題
- `st.write` 用於顯示多種格式的內容
- `st.text` 用於顯示純文字
- `st.markdown` 用於顯示支持 Markdown 語法的內容
