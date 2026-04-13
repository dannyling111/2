const sendBtn = document.getElementById('sendBtn');
const apiKeyInput = document.getElementById('apiKey');
const promptInput = document.getElementById('prompt');
const resultEl = document.getElementById('result');

sendBtn.addEventListener('click', async () => {
  const apiKey = apiKeyInput.value.trim();
  const prompt = promptInput.value.trim();

  if (!apiKey) {
    resultEl.textContent = '请先输入 DeepSeek API Key。';
    return;
  }

  if (!prompt) {
    resultEl.textContent = '请先输入提问内容。';
    return;
  }

  sendBtn.disabled = true;
  resultEl.textContent = '请求中...';

  try {
    const resp = await fetch('https://api.deepseek.com/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: 'deepseek-chat',
        messages: [
          {
            role: 'user',
            content: prompt,
          },
        ],
        temperature: 0.7,
      }),
    });

    if (!resp.ok) {
      const errText = await resp.text();
      throw new Error(`请求失败: ${resp.status} ${errText}`);
    }

    const data = await resp.json();
    const content = data?.choices?.[0]?.message?.content || '没有返回内容。';
    resultEl.textContent = content;
  } catch (err) {
    resultEl.textContent = `出错了：${err.message}`;
  } finally {
    sendBtn.disabled = false;
  }
});
