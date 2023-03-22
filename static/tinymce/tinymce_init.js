document.addEventListener('DOMContentLoaded', function () {
    tinymce.init({
        selector: '.tinymce',
        plugins: 'image link fullscreen anchor autoresize autosave code lists media wordcount table preview',
        toolbar: 'image link fullscreen anchor autoresize restoredraft code numlist bullist media wordcount table preview',
        table_toolbar: 'tableprops tabledelete | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol',
        skin: 'oxide-dark',
        content_css: 'dark',
    });
})