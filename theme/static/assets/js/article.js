window.addEventListener('DOMContentLoaded', function() {
    // Get the hidden input field
    var hiddenInput = document.getElementById('hidden-input');
    var articlesContainer = document.getElementsByClassName('row my-5')[0];
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
                <div class="col-lg-4 py-3">
                  <div class="card-blog">
                    <div class="header">
                      <div class="post-thumb">
                        <img loading="lazy" src="${article.SITEURL}/${article.thumbnail}" alt="${article.alt || ''}">
                      </div>
                    </div>
                    <div class="body">
                      <h5 class="post-title"><a href="${article.slug}">${article.title}</a></h5>
                      <div class="post-date">Posted on <a href="#">${article.date}</a></div>
                      ${article.resume ? `<p>${article.resume}</p>` : ''}
                    </div>
                  </div>
                </div>`;
                articlesContainer.insertAdjacentHTML('beforeend', articleHtml);
            }
            // Show load more button if more articles exist
            if (inputArray.length > 6 && endIndex < inputArray.length) {
                loadMoreButton.style.display = 'block';
            } else {
                loadMoreButton.style.display = 'none';
            }
        }
  
        // Initial display of articles
        displayArticles(0, 6);
  
        // Load more button click event
        loadMoreButton.addEventListener('click', function() {
          var startIndex = articlesContainer.children.length;
          var endIndex = startIndex + 6;
          displayArticles(startIndex, endIndex);
        });
    }
  });