import pymupdf as fitz
import re

def extract_and_clean_v2():
    pdf_path = 'test.pdf'
    doc = fitz.open(pdf_path)
    full_text = ''

    for page_num in range(len(doc)):
        page = doc[page_num]
        full_text += page.get_text('text')+'\n'
    doc.close()

    #  把所有换行符替换成空格，把整篇文段变成连续的一长串
    text = full_text.replace('\n','')

    #  用暴力正则删除常见的版权废话
    junk_work = [
        r'"Just Accepted".*?manuscripts\.',
        r'Prepared for submission.*?Chemistry',
        r'Downloaded from.*?ACS.*?',
        r'\b\d+\b'  #  删除所有孤立的数字
    ]
    for pattern in junk_work:
        text = re.sub(pattern,'',text,flags=re.DOTALL)

    #   把多个连续的空格变成一个空格
    text = re.sub(r'\+','',text)

    #   ===========核心：按句子切片===========
    #   不能按固定数切，要按句子切（找句号.问号?感叹号！作为分隔符）
    #   这样切出来的每个片段，语义是完整的
    sentences = re.split(r'(?<=[.!?])\s+',text)

    chunks = []
    current_chunk = ''
    max_length = 500
    for sentence in sentences:
        # 如果加上这句话没超长，就拼在一起
        if len(current_chunk) +len(sentence) <max_length:
            current_chunk += sentence + ''
        else:
            #超长了，就把当前的存起来，重新开一个碎片
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence + ''

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    # 过滤掉太短的碎片（比如少于50字的，大概率是垃圾，过滤掉）
    chunks = [c for c in chunks if len(c) > 50]

    print(f'高级清洗完毕，共{len(chunks)} 片')
    print(f'第5片段\n{chunks[4]}')



if __name__ == '__main__':
    extract_and_clean_v2()









