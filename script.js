async function submitPost() {
    const postContent = document.getElementById('postInput').value;
    if (postContent.trim() === '') return;
  
    const response = await fetch('/api/posts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content: postContent }),
    });
  
    if (response.ok) {
      document.getElementById('postInput').value = '';
      loadFeed();
    }
  }
  
  async function loadFeed() {
    const response = await fetch('/api/posts');
    const posts = await response.json();
    const feed = document.getElementById('feed');
    feed.innerHTML = posts.map(post => `<p>${post.content}</p>`).join('');
  }
  
  window.onload = loadFeed;
  