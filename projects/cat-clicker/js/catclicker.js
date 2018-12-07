var CatClicker = (function () {
    var model = {
        currentCat: null,
        cats: [
            {
                name: 'Bob',
                imageFile: '0001.jpg',
                clicks: 0
            },
            {
                name: 'Mili',
                imageFile: '0002.jpg',
                clicks: 0
            },
            {
                name: 'Teddy and Sofy',
                imageFile: '0003.jpg',
                clicks: 0
            },
            {
                name: 'Wolf',
                imageFile: '0004.jpg',
                clicks: 0
            },
            {
                name: 'Morgan',
                imageFile: '0005.jpg',
                clicks: 0
            }
        ]
    };

    var octopus = {
        init: function () {
            model.currentCat = model.cats[0];
            catListView.init();
            catView.init();
        },

        addCat: function (name, imageFile) {
            model.cats.push({
                name: name,
                imageFile: imageFile,
                clicks: 0
            });
        },

        addClick: function () {
            var cat = octopus.getCurrentCat();
            cat.clicks++;
            catView.renderClicks();
        },

        editCurrentCat: function (name, imageFile, clicks) {
            var cat = octopus.getCurrentCat();

            cat.name = name;
            cat.imageFile = imageFile;
            cat.clicks = clicks;

            catView.renderInfo();
            catListView.render();
        },

        getCats: function () {
            return model.cats;
        },

        getCurrentCat: function () {
            return model.currentCat;
        },

        setCurrentCat: function (cat) {
            model.currentCat = cat;
            catView.renderInfo();
        }
    };

    var catView = {
        init: function () {
            var catForm, catInfo;

            // Cat Info
            this.catInfo = {
                name:       document.getElementById('cat-name'),
                image:      document.getElementById('cat-image'),
                clicks:     document.getElementById('cat-clicks'),
                edit:       document.getElementById('btn-edit'),
                container:  document.getElementById('cat-info')
            };
            catInfo = this.catInfo;

            // Cat Form
            this.catForm = {
                name:       document.getElementById('input-name'),
                image:      document.getElementById('input-image'),
                clicks:     document.getElementById('input-clicks'),
                save:       document.getElementById('btn-save'),
                cancel:     document.getElementById('btn-cancel'),
                container:  document.getElementById('cat-form')
            };
            catForm = this.catForm;

            // Hidden Form
            catView.hideShowElement('hide', catForm);

            // Listeners
            this.catInfo.image.addEventListener('click', function () {
                octopus.addClick();
            });

            this.catInfo.edit.addEventListener('click', function () {
                catView.hideShowElement('show', catForm);
                catView.hideShowElement('hide', catInfo);
                catView.fillForm();
            });

            this.catForm.cancel.addEventListener('click', function () {
                catForm.container.reset();
                catView.hideShowElement('hide', catForm);
                catView.hideShowElement('show', catInfo);
            });

            this.catForm.save.addEventListener('click', function () {
                var values = catView.getFormValues();
                
                octopus.editCurrentCat(values.name, values.image, values.clicks);
                catView.hideShowElement('hide', catForm);
                catView.hideShowElement('show', catInfo);
            });

            // Render
            catView.renderInfo();
        },

        renderClicks: function () {
            var info = this.catInfo,
                cat = octopus.getCurrentCat();

            info.clicks.textContent = cat.clicks;
        },

        renderInfo: function () {
            var info = this.catInfo,
                cat = octopus.getCurrentCat();

            info.name.textContent = cat.name;
            info.image.src = 'images/' + cat.imageFile;
            catView.renderClicks();
        },

        fillForm: function () {
            var form = this.catForm,
                cat = octopus.getCurrentCat();

            form.name.value = cat.name;
            form.image.value = cat.imageFile;
            form.clicks.value = cat.clicks;
        },

        getFormValues: function () {
            var form = this.catForm;

            return {
                name: form.name.value,
                image: form.image.value,
                clicks: form.clicks.value
            };
        },

        hideShowElement: function (status, elm) {
            switch (status) {
                case 'show':
                    elm.container.style.display = "block";
                    break;
                case 'hide':
                    elm.container.style.display = "none";
                    break;
            }
        }
    };

    var catListView = {
        init: function () {
            this.catList = document.getElementById('cat-list');
            catListView.render();
        },

        putListening: function (target, cat) {
            target.addEventListener('click', function () {
                octopus.setCurrentCat(cat);
            });
        },

        render: function () {
            var list = this.catList;

            list.textContent = '';
            octopus.getCats().forEach(function (cat) {
                var li = document.createElement('li');
                li.textContent = cat.name;
                catListView.putListening(li, cat);
                list.appendChild(li);
            });
        }
    };

    return {
        addCat: octopus.addCat,
        init: octopus.init
    };
}());

CatClicker.init();
