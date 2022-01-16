$(document).ready(function () {
    totalCart()

    function totalCart() {
        $.ajax({
            url: "/total_cart",

            success: function (res) {
                document.getElementById('total-cart').innerText = res
            }
        });
    }
    $(document).on('click', ".add-cwishlist", function () {
        var _pid = $(this).attr('data-product');

        // Ajax
        $.ajax({
            url: "/add_to_course_wishlist",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function (res) {
                // swal(res.string)
            }
        });
        // EndAjax
    });

    $(document).on('click', ".add-bwishlist", function () {
        var _pid = $(this).attr('data-product');

        // Ajax
        $.ajax({
            url: "/add_to_book_wishlist",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function (res) {
                // swal(res.string)
            }
        });
        // EndAjax

    });

    $(document).on('click', ".add-twishlist", function () {
        var _pid = $(this).attr('data-product');

        // Ajax
        $.ajax({
            url: "/add_to_test_wishlist",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function (res) {
                // swal(res.string)
            }
        });
        // EndAjax

    });

    $(document).on('click', ".add-ccart", function () {
        var _pid = $(this).attr('data-product');

        // Ajax
        $.ajax({
            url: "/add_to_course_cart",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function (res) {
                totalCart()
                // swal(res.string)

            }
        });
    });

    $(document).on('click', ".add-tcart", function () {
        var _pid = $(this).attr('data-product');

        // Ajax
        $.ajax({
            url: "/add_to_test_cart",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function (res) {
                totalCart()
                // swal(res.string)

            }
        });
        // EndAjax

    });
    $(document).on('click', ".buynow", function () {
        var _pid = $(this).attr('data-product');

        // Ajax
        $.ajax({
            url: "/add_to_course_cart",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function (res) {
                totalCart()
                window.location.href = '/shopping_cart'

            }
        });
        // EndAjax

    });

    $(document).on('click', ".add-bcart", function () {
        var _pid = $(this).attr('data-product');
        var _qty = $(this).attr('data-qty');

        // Ajax
        $.ajax({
            url: "/add_to_book_cart",
            data: {
                product: _pid,
                qty: _qty,
            },
            dataType: 'json',
            success: function (res) {
                totalCart()
                // swal(res.string)
            }

        });
        // EndAjax

    });

    $(document).on('click', ".add-bcart1", function () {
        var _pid = $(this).attr('data-product');
        var _qty = document.getElementById('bookCount1').value;

        // Ajax
        $.ajax({
            url: "/add_to_book_cart",
            data: {
                product: _pid,
                qty: _qty,
            },
            dataType: 'json',
            success: function (res) {
                totalCart()
                // swal(res.string)
            }
        });
        // EndAjax

    });

    $(document).on('click', ".edit-mark", function () {
        var sid = $(this).data('id');
        var mark = $(this).data('mark');


        $('.MarkModal #sid').val(sid);
        $('.MarkModal #obtain_mark').val(mark);



    });

    $(document).on('click', ".start-test", function () {
        var sid = $(this).data('id');
        var mid = $(this).data('mid');
        $('#tid').val(sid);
        $('#mid').val(mid);

    });





});