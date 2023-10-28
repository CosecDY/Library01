function createTopBooks(bookData) {
  const container = document.createElement('div');
  container.style.display = 'flex';
  container.style.flexDirection = 'column'; 

  const h1 = document.createElement('h1');
  h1.textContent = "Popular books";
  h1.style.textAlign = 'center';
  h1.style.marginBottom = '30px';
  h1.style.fontSize = '45px';

  container.appendChild(h1);

  const topBooksContainer = document.createElement('div');
  topBooksContainer.className = 'top_books';

  const frame = document.createElement('div');
  frame.style.border = '2px solid #ccc';
  frame.style.borderRadius = '10px';
  frame.style.padding = '20px';
  frame.style.maxWidth = '2400px';
  frame.style.margin = '0 auto';
  frame.style.width = '1500px';
  frame.style.boxShadow = '0 0 5px #089da1';

  const topBookBox = document.createElement('div');
  topBookBox.className = 'top_book_box';
  topBookBox.style.display = 'flex';
  topBookBox.style.justifyContent = 'center';
  topBookBox.style.width = '100%';
  topBookBox.style.padding = '0 20px';
  topBookBox.style.display = 'grid';
  topBookBox.style.overflow = 'hidden';

  bookData.forEach((bookInfo) => {
    const bookCard = document.createElement("div");
    bookCard.className = "book-card";
    bookCard.style.width = '800px';
    bookCard.style.borderRadius = '10px';
  
    const bookTag = document.createElement('div');
    bookTag.className = 'top_book_tag';
    bookTag.style.display = 'flex';
    bookTag.style.justifyContent = 'space-between';
    bookTag.style.alignItems = 'center';
    bookTag.style.margin = '10px 0';
  
    const bookInfoContainer = document.createElement('div');
    bookInfoContainer.className = 'book-info-container';
    bookInfoContainer.style.display = 'flex';
    bookInfoContainer.style.justifyContent = 'space-evenly';
    bookInfoContainer.style.alignItems = 'center';
    bookInfoContainer.style.width = '100%';
  
    const bookTitle = document.createElement("div");
    bookTitle.className = "book-title";
    bookTitle.textContent = bookInfo.nameBook;
  
    const bookCategory = document.createElement("div");
    bookCategory.className = "book-category";
    bookCategory.textContent = `Category: ${bookInfo.category}`;
    bookCategory.style.margin = '0 auto';
  
    const bookLikes = document.createElement("div");
    bookLikes.className = "book-likes";
    bookLikes.textContent = `Likes: ${bookInfo.totalLikes}`;
  
    bookInfoContainer.appendChild(bookTitle);
    bookInfoContainer.appendChild(bookCategory);
    bookInfoContainer.appendChild(bookLikes);
  
    bookTag.appendChild(bookInfoContainer);
  
    bookCard.appendChild(bookTag);
  
    topBookBox.appendChild(bookCard);
  });

  topBooksContainer.appendChild(topBookBox);
  frame.appendChild(topBooksContainer);
  container.appendChild(frame);

  return container;
}

fetch('/api/top_book_data')
  .then(response => response.json())
  .then(data => {
    const topBook = createTopBooks(data.data);
    document.body.appendChild(topBook);
  })
  .catch(error => {
    console.error('เกิดข้อผิดพลาดในการดึงข้อมูล:', error);
  });
  










  function sendDataToFlask(data, url, successCallback, errorCallback) {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('ไม่สามารถส่งข้อมูลไปยัง Flask');
        }
    })
    .then(data => {
        successCallback(data);
    })
    .catch(error => {
        errorCallback(error);
    });
}


function createFeaturedBooks(bookData, categories) {
    const featuredBooksContainer = document.createElement('div');
    featuredBooksContainer.className = 'featured_boks';

    featuredBooksContainer.style.width = '100%';
    featuredBooksContainer.style.height = '100vh';
    featuredBooksContainer.style.padding = '70px 0';
    featuredBooksContainer.style.overflowX = 'auto'; 

    const h1 = document.createElement('h1');
    h1.textContent = categories;
    h1.style.display = 'flex';
    h1.style.textAlign = 'center';
    h1.style.marginBottom = '30px';
    h1.style.fontSize = '45px';

    featuredBooksContainer.appendChild(h1);

    const featuredBookBox = document.createElement('div');
    featuredBookBox.className = 'featured_book_box';
    featuredBookBox.style.display = 'flex';
    featuredBookBox.style.width = '100%';
    featuredBookBox.style.padding = '0 20px';
    featuredBookBox.style.display = 'grid';
    featuredBookBox.style.overflow = 'hidden';
    featuredBookBox.style.overflowX = 'scroll';

    bookData.forEach((bookInfo) => {
      const featuredBookCard = document.createElement('div');
      featuredBookCard.className = 'featured_book_card';
      featuredBookCard.style.width = '250px';
      featuredBookCard.style.height = '390px';
      featuredBookCard.style.textAlign = 'center';
      featuredBookCard.style.padding = '5px';
      featuredBookCard.style.border = '1px solid #919191';
      featuredBookCard.style.margin = 'auto 20px';
  
      featuredBookCard.addEventListener('mouseover', function () {
          featuredBookCard.style.boxShadow = '0 0 5px #089da1';
      });
  
      featuredBookCard.addEventListener('mouseout', function () {
          featuredBookCard.style.boxShadow = 'none';
      });
  
      const bookImage = document.createElement('div');
      bookImage.className = 'featured_book_img';
      const img = document.createElement('img');
      img.src = bookInfo.imgSrc;
      img.style.width = '170px';
  
      bookImage.appendChild(img);
  
      const bookTag = document.createElement('div');
      bookTag.className = 'featurde_book_tag';
  
      const h2 = document.createElement('h3');
      h2.textContent = bookInfo.nameBook;
  
      const writer = document.createElement('p');
      writer.className = 'writer';
      writer.textContent = bookInfo.writer;
  
      const categories = document.createElement('div');
      categories.className = 'categories';
      categories.textContent = bookInfo.categories;
  
      const bookPrice = document.createElement('p');
      bookPrice.className = 'book_price';
      bookPrice.innerHTML = `${bookInfo.price} ฿<sub><del>`;
  
      const learnMoreLink = document.createElement('a');
      learnMoreLink.className = 'f_btn';
      learnMoreLink.href = bookInfo.learnMoreLink;
      learnMoreLink.textContent = 'Learn More';
      learnMoreLink.addEventListener('click', function(event) {
        event.preventDefault();  
        sendDataToFlask(bookInfo, '/receive_data', function(responseData) {
            console.log('รับข้อมูลจาก Flask:', responseData);
        }, function(error) {
            console.error('เกิดข้อผิดพลาดในการส่งข้อมูล:', error);
        });
    });

      const totalLikesElement = document.createElement('div');
      totalLikesElement.className = 'total_likes';
      totalLikesElement.textContent = `Likes ${bookInfo.totalLikes}`;
      totalLikesElement.style.fontSize = '14px';
      totalLikesElement.style.marginTop = '15px';
      totalLikesElement.style.fontWeight = 'bold';
  
      bookTag.appendChild(h2);
      bookTag.appendChild(writer);
      bookTag.appendChild(categories);
      bookTag.appendChild(bookPrice);
      bookTag.appendChild(learnMoreLink);
      bookTag.appendChild(totalLikesElement);
  
      featuredBookCard.appendChild(bookImage);
      featuredBookCard.appendChild(bookTag);
  
      featuredBookBox.appendChild(featuredBookCard);
  });
    featuredBooksContainer.appendChild(featuredBookBox);

    return featuredBooksContainer;
}

fetch('/api/book_data')
  .then(response => response.json())
  .then(data => {

    const bookDataComic = data.data[0];
    const bookDataFiction = data.data[1];
    const bookDataHorror = data.data[2];
    const bookDataLearning = data.data[3];
    const bookDataRomance = data.data[4];

    const featuredBooksComic = createFeaturedBooks(bookDataComic, 'Comic');
    document.body.appendChild(featuredBooksComic);
    const featuredBooksFiction = createFeaturedBooks(bookDataFiction, 'Fiction');
    document.body.appendChild(featuredBooksFiction);
    const featuredBooksHorror = createFeaturedBooks(bookDataHorror, 'Horror');
    document.body.appendChild(featuredBooksHorror);
    const featuredBooksLearning = createFeaturedBooks(bookDataLearning, 'Learning');
    document.body.appendChild(featuredBooksLearning);
    const featuredBooksRomance = createFeaturedBooks(bookDataRomance, 'Romance');
    document.body.appendChild(featuredBooksRomance);

  })
  .catch(error => {
    console.error('เกิดข้อผิดพลาดในการดึงข้อมูล:', error);
  });
  

  





