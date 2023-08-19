//function save() {
//var checkbox = document.getElementById("color");
//localStorage.setItem("color", checkbox.checked);
//}
//
////for loading
//let checked;
//try {
//  checked = JSON.parse(localStorage.getItem("color"));
//} catch(e) {
//  checked = false; // default value on error
//  if (typeof e === 'object' && e.message) {
//    console.error(e.message)
//  }
//}
//document.getElementById("color").checked = checked;




//
//const checkbox1 = document.getElementById('color-all');
////const checkbox2 = document.getElementById('2');
//const checkbox2 = document.querySelectorAll('[name="colors"]');
//
//checkbox1.addEventListener('change', () => {
//  if (checkbox1.checked) {
//    checkbox2.checked = false;
//  }
//});
//
//checkbox2.addEventListener('change', () => {
//  if (checkbox2.checked) {
//    checkbox1.checked = false;
//  }
//});




//// Получаем все чекбоксы, которые относятся к одной группе
//const checkboxes = document.querySelectorAll('input[type="checkbox"][name="colors"]');
//const checkbox = document.getElementById('color-all');
//
//// Добавляем обработчик событий для каждого чекбокса
//checkboxes.forEach(function(checkbox) {
//  checkbox.addEventListener('click', function() {
//    // Если этот чекбокс отмечен, то отжимаем все остальные в группе
//    if (checkbox.checked) {
//      checkboxes.forEach(function(otherCheckbox) {
//        if (otherCheckbox !== checkbox) {
//          otherCheckbox.checked = false;
//        }
//      });
//    }
//  });
//});





//// Получаем все чекбоксы, которые нужно контролировать
//const checkboxesGroup1 = document.querySelectorAll('[name="colors"]');
//const checkboxesGroup2 = document.querySelectorAll('[name="colors"]');
//
//// Функция для отжатия всех чекбоксов в группе
//function uncheckGroup(checkboxes) {
//  checkboxes.forEach((checkbox) => {
//    checkbox.checked = false;
//  });
//}
//
//// Обработчик события "изменение состояния чекбокса"
//function onCheckboxChange(event) {
//  const targetCheckbox = event.target;
//
//  // В зависимости от группы, в которой находится чекбокс, отжимаем другие чекбоксы
//  if (targetCheckbox.classList.contains('[name="color"]')) {
//    uncheckGroup(checkboxesGroup2);
//  } else if (targetCheckbox.classList.contains('[name="colors"]')) {
//    uncheckGroup(checkboxesGroup1);
//  }
//}
//
//// Назначаем обработчик события всем чекбоксам
//checkboxesGroup1.forEach((checkbox) => {
//  checkbox.addEventListener('change', onCheckboxChange);
//});
//checkboxesGroup2.forEach((checkbox) => {
//  checkbox.addEventListener('change', onCheckboxChange);
//});




//// Получаем коллекции чекбоксов для каждой группы
//const group1 = document.querySelectorAll('.group1 input[type="checkbox"]');
//const group2 = document.querySelectorAll('.group2 input[type="checkbox"]');
//
//// Создаем функцию для обработчика события
//function handleCheckbox(event) {
//  const target = event.target;
//  if (target.checked) {
//    if (group1.includes(target)) {
//      group2.forEach(checkbox => checkbox.checked = false);
//    } else if (group2.includes(target)) {
//      group1.forEach(checkbox => checkbox.checked = false);
//    }
//  }
//}
//
//// Присваиваем обработчик события для каждого чекбокса
//group1.forEach(checkbox => checkbox.addEventListener('change', handleCheckbox));
//group2.forEach(checkbox => checkbox.addEventListener('change', handleCheckbox));




// получаем все checkbox из двух групп цветов
const color1 = document.querySelectorAll('[name="color"]');
const color2 = document.querySelectorAll('[name="colors"]');

// добавляем обработчик клика на все checkbox из первой группы
color1.forEach(checkbox => {
  checkbox.addEventListener('click', () => {
    // снимаем выделение со всех checkbox из второй группы
    color2.forEach(checkbox => {
      checkbox.checked = false;
    });
  });
});

// добавляем обработчик клика на все checkbox из второй группы
color2.forEach(checkbox => {
  checkbox.addEventListener('click', () => {
    // снимаем выделение со всех checkbox из первой группы
    color1.forEach(checkbox => {
      checkbox.checked = false;
    });
  });
});


// получаем все checkbox из двух групп размеров
const size1 = document.querySelectorAll('[name="size"]');
const size2 = document.querySelectorAll('[name="sizes"]');

// добавляем обработчик клика на все checkbox из первой группы
size1.forEach(checkbox => {
  checkbox.addEventListener('click', () => {
    // снимаем выделение со всех checkbox из второй группы
    size2.forEach(checkbox => {
      checkbox.checked = false;
    });
  });
});

// добавляем обработчик клика на все checkbox из второй группы
size2.forEach(checkbox => {
  checkbox.addEventListener('click', () => {
    // снимаем выделение со всех checkbox из первой группы
    size1.forEach(checkbox => {
      checkbox.checked = false;
    });
  });
});


// $("#custom-control custom-checkbox d-flex align-items-center justify-content-between mb-3 :checkbox").on("change", function(){ alert("The checkbox with the ID '" + this.id + "' changed"); });


//// Получаем все checkbox на странице
//const checkboxes = document.querySelectorAll('input[type=checkbox]');
//
//// Для каждого checkbox добавляем обработчик события "change"
//checkboxes.forEach(checkbox => {
//  checkbox.addEventListener('change', () => {
//    // При изменении состояния checkbox сохраняем его значение в localStorage
//    localStorage.setItem(checkbox.id, checkbox.checked);
//  });
//
//  // Проверяем, сохранено ли значение checkbox в localStorage
//  const checked = localStorage.getItem(checkbox.id) === 'true';
//
//  // Если значение сохранено, устанавливаем соответствующее состояние checkbox
//  if (checked) {
//    checkbox.checked = true;
//  }
//});




//// Получить элемент строки поиска
//var searchInput = document.getElementById("search");
//
//// Получить значение из localStorage
//var savedValue = localStorage.getItem("search-value");
//
//// Если значение сохранено, установить его в input
//if (savedValue) {
//  searchInput.value = savedValue;
//}
//
//// Сохранить значение строки поиска в localStorage при изменении
//searchInput.addEventListener("input", function() {
//  localStorage.setItem("search-value", searchInput.value);
//});