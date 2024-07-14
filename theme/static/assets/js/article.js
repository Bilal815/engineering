window.addEventListener('DOMContentLoaded', function() {
  // Get the hidden input field
  var hiddenInput = document.getElementById('hidden-input');
  var articlesContainer = document.getElementById('articles-container');
  var loadMoreButton = document.getElementById('load-more-button'); 

  // Check if hiddenInput exists
  if (hiddenInput) {
      // Get the JSON value from the hidden input field
      var inputValueJson = hiddenInput.value;

      // Parse the JSON value
      var inputArray = JSON.parse(inputValueJson);

      // Function to display articles
      function displayArticles(startIndex, endIndex) {
          // Display articles within the specified range
          for (var i = startIndex; i < endIndex && i < inputArray.length; i++) {
              var article = inputArray[i];
              var articleHtml = `
              <div class="col-lg-6">
                <div class="blog-post">
                  <div class="blog-thumb">
                    <img loading="lazy" src="${article.SITEURL}/${article.thumbnail}" alt="${article.alt || ''}">
                  </div>
                  <div class="down-content">
                    <span>${article.category}</span>
                    <a href="${article.SITEURL}/${article.slug}"><h4>${article.title}</h4></a>
                    <ul class="post-info">
                      ${article.author.map(author => `<li><a href="${author.url}">${author.name}</a></li>`).join('')}
                      <li><a href="">${article.date}</a></li>
                    </ul>
                    ${article.resume ? `<p>${article.resume}</p>` : ''}
                    <div class="post-options">
                      <ul class="post-tags">
                        <li>
                          <i class="fa fa-tags"></i>
                        </li>
                        ${article.tags.map((tag, index) => `<li><a href="${tag.url}">${tag.name}</a>${index !== article.tags.length - 1 ? ' , ' : ''}</li>`).join(' ')}
                      </ul>
                    </div>
                  </div>
                </div>
              </div>`;
              articlesContainer.insertAdjacentHTML('beforeend', articleHtml);
          }

          // Show load more button if more articles exist
          if (inputArray.length > 7 && endIndex < inputArray.length) {
              loadMoreButton.style.display = 'block';
          } else {
              loadMoreButton.style.display = 'none';
          }
      }

      // Initial display of articles
      displayArticles(0, 7);

      // Load more button click event
      loadMoreButton.addEventListener('click', function() {
        var startIndex = articlesContainer.children.length;
        var endIndex = startIndex + 7;
        displayArticles(startIndex, endIndex);
      });
  }
});