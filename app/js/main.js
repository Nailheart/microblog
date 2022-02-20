(() => {
  // Переключения навигации
  const nav = document.querySelector('.nav');
  if (nav) {
    const navToggle = nav.querySelector('.nav__toggle');
    navToggle.addEventListener('click', () => {
      nav.classList.toggle('nav--active');
      document.querySelector('body').style.overflow = 'hidden';
    });
  }

  // Отображения попапа при наведении на имя пользователя
  let timer = null;
  let xhr = null;
  const posts = document.querySelectorAll('.post');
  if (posts) {
    posts.forEach((post) => {
      const post_popup = post.querySelector('.post__popup');
      const post_author = post.querySelector('.post__author');
      const tooltip = post.querySelector('.tooltip');

      post_popup.addEventListener('mouseenter', () => {
        timer = setTimeout(() => {
          timer = null;
          xhr = fetch('/user/' + post_author.textContent.trim() + '/popup')
            .then((data) => data.text())
            .then((popupHTML) => {
              xhr = null;
              tooltip.insertAdjacentHTML('beforeend', popupHTML);
              
              // отображаем попап
              show();

              // когда новые элементы Flask-Moment добавляются через Ajax, необходимо вызвать функцию
              // flask_moment_render_all() для правельного отображения этих элементов.
              flask_moment_render_all();
            });
        }, 1000);
      });
      post_popup.addEventListener('mouseleave', () => {
        if (timer) {
          clearTimeout(timer);
          timer = null;
        } else if (xhr) {
          xhr.abort();
          xhr = null;
        } else {
          // скрываем попап
          hide();
        }
      });

      // popper Instance
      const popperInstance = Popper.createPopper(post_popup, tooltip, {
        placement: 'right',
        // modifiers: [
        //   {
        //     name: 'offset',
        //     options: {
        //       offset: [0, 8],
        //     },
        //   },
        // ],
      });

      function show() {
        // Make the tooltip visible
        tooltip.setAttribute('data-show', '');

        // Enable the event listeners
        popperInstance.setOptions((options) => ({
          ...options,
          modifiers: [
            ...options.modifiers,
            { name: 'eventListeners', enabled: true },
          ],
        }));
      
        // We need to tell Popper to update the tooltip position
        // after we show the tooltip, otherwise it will be incorrect
        popperInstance.update();
      }
      
      function hide() {
        // Hide the tooltip
        tooltip.removeAttribute('data-show');
        tooltip.removeChild(tooltip.lastChild);

        // Disable the event listeners
        popperInstance.setOptions((options) => ({
          ...options,
          modifiers: [
            ...options.modifiers,
            { name: 'eventListeners', enabled: false },
          ],
        }));
      }
    });
  }
})();