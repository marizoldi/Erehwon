;(function() {

  var Tags = (function() {

    // Wrapper and Input vars
    var tagsContainer,
    tagsInput,
    removeBtn = {},
    // value
    val,

    // keyboard
    KEYS = {
      ENTER: 13,
      COMMA: 188,
      BACK: 8
    },

    // Focus event through settimeout
    timer,

    // Tags array
    tagsArray = {},

    // globalEvents
    // handlerClick,
    handlerKey = [],
    handlerClick = [],

    // HTML wrapper
    html = '<input class="tag-input"></input>';


    function init(selector, options) {
      if(selector.trim() === '') return;

      [].forEach.call( qsa(selector), function(originInput, index) {

        removeBtn[index] = originInput.getAttribute('data-removeBtn');

        // create and add wrapper
        var wrap = create('div', {
          'className': 'tags-container',
          'innerHTML': html
        });
      
        var placeholder = originInput.getAttribute('placeholder');
        if(placeholder)
          wrap.querySelector('input').setAttribute('placeholder', placeholder);

        originInput.style.display = 'none';

        tagsArray[index] = [];

        originInput.parentNode.insertBefore(wrap, originInput.nextSibling);

        // if input exist values by default
        if(originInput.value !== '') {
          notEmpty(originInput, index);
        }

        bindEventKey(wrap, originInput, index);
        removeBtn[index] && removeByClick(wrap, originInput, index);
      });

    }

    function bindEventKey(wrap, originInput, index) {
      handlerKey[index] = function(evt) {
        if(evt.target.tagName === 'INPUT' && evt.target.className === 'tag-input') {
          tagsInput = evt.target;
          tagsContainer = tagsInput.parentNode;
          var code = evt.keyCode;

          val = tagsInput.value.trim();

          if(code === KEYS.ENTER || code === KEYS.COMMA) {
            evt.target.blur();
            if(code === KEYS.COMMA) evt.preventDefault();

            addTag(originInput, index);

            if(timer) clearTimeout(timer);
            timer = setTimeout(function() { evt.target.focus(); }, 10 );
          }
          else if(code === KEYS.BACK) {
            removeTag(originInput, index);
          }
        }
      };
      wrap.addEventListener('keydown', handlerKey[index], false);
    }
    function removeByClick(wrap, originInput, index) {

        handlerClick[index] = function(evt) {
          if(evt.target.className === 'remove-tag') {
            var container = evt.target.parentNode.parentNode,
                input     = container.querySelector('input'),
                name      = evt.target.parentNode.getAttribute('data-tag');

            container.removeChild(evt.target.parentNode);

            tagsArray[index].splice( tagsArray[index].indexOf(name), 1);
            originInput.value = tagsArray[index].join(',');

            input.focus();
          }
        };
        wrap.addEventListener('click', handlerClick[index], false);
    }

    function notEmpty(originInput, index) {
      var arr = originInput.value.split(',');
      var frag = document.createDocumentFragment();
      arr.forEach(function(item) {
        var tag = createTag(item, index);
        tagsArray[index].push(item);
        frag.appendChild(tag);
      });
      originInput.nextSibling.insertBefore(frag, originInput.nextSibling.querySelector('input'));
    }

    function createTag(item, index) {
      var tag = create('div', {
        'className': 'tag',
        'textContent': item
      });
      if(removeBtn[index]) {
        addClass('tag-padding-btn', tag);
        tag.setAttribute('data-tag', item);
        tag.innerHTML += '<span class="remove-tag">&times;</span>';
      }
      return tag;
    }

    function addTag(originInput, index) {

      // delete comma if comma exists
      val = val.replace(/,/g, '').trim();

      if(val === '') return tagsInput.value = '';

      if(tagsArray[index].indexOf(val) > -1) {

        var exist = null;

        exist = qsa('.tag', tagsContainer);

        [].forEach.call(exist, function(tag) {
          if(tag.firstChild.textContent === val) {

            addClass('exist', tag);

            if(whichTransitionEnd()) {
              tag.oneEventListener(whichTransitionEnd(), function() {
                removeClass('exist', this);
              });
            }
            else {
              setTimeout(function() {
                removeClass('exist', tag);
              }, 150);
            }

          }

        });

        return tagsInput.value = '';
      }

      var tag = createTag(val, index);

      tagsInput.parentNode.insertBefore(tag, tagsInput);
      tagsArray[index].push(val);
      tagsInput.value = '';
      originInput.value += (originInput.value === '') ? val : ',' + val;
    }

    function removeTag(originInput, index) {

      if(val !== '' || tagsArray[index].length === 0) return;
      var name = tagsArray[index].pop();

      if(tagsInput.previousSibling) {
        tagsContainer.removeChild(tagsInput.previousSibling);
      }

      originInput.value = tagsArray[index].join(',');
    }

    // Destroy
    function destroy() {
      var tagsContainer = qsa('.tags-container');

      [].forEach.call(tagsContainer, function(container, index) {
        container.removeEventListener('keydown', handlerKey[index], false);
        removeBtn && container.removeEventListener('click', handlerClick[index], false);
        container.previousSibling.removeAttribute('style');
        container.parentNode.removeChild(container);
      });
    }

    // Helpers
    function create(el, attr) {
      var element = document.createElement(el);
      if(attr) {
        for(var name in attr) {
          if(element[name] !== undefined) {
            element[name] = attr[name];
          }
        }
      }
      return element;
    }

    function whichTransitionEnd() {
      var root = document.documentElement;
      var transitions = {
        'transition'       : 'transitionend',
        'WebkitTransition' : 'webkitTransitionEnd',
        'MozTransition'    : 'mozTransitionEnd',
        'OTransition'      : 'oTransitionEnd otransitionend'
      };

      for(var t in transitions){
        if(root.style[t] !== undefined){
          return transitions[t];
        }
      }
      return false;
    }

    function qsa(selector, context) {
      return ((context) ? context : document).querySelectorAll(selector);
    }

    if(Element.prototype.addEventListener) {
      Element.prototype.oneEventListener = function(type, cb) {

        var self = this;

        var handler = function(e) {
          self.removeEventListener(e.type, handler, false);
          cb.bind(self, e).call();
        };
        self.addEventListener(type, handler, false);
      };
    }

    // class helpers
    function hasClass(cls, el) {
      return new RegExp('(^|\\s+)' + cls + '(\\s+|$)').test(el.className);
    }
    function addClass(cls, el) {
      if( ! hasClass(cls, el) )
        return el.className += (el.className === '') ? cls : ' ' + cls;
    }
    function removeClass(cls, el) {
      el.className = el.className.replace(new RegExp('(^|\\s+)' + cls + '(\\s+|$)'), '');
    }
    function toggleClass(cls, el) {
      ( ! hasClass(cls, el)) ? addClass(cls, el) : removeClass(cls, el);
    }

    return {
      init: init,
      destroy: destroy
    };

  })();


  Tags.init('.tagged');


})();