'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

// console.log("hello, iat!");

var Category = function Category(round_number, left_main_category, right_main_category, left_sub_category, right_sub_category, left_keycode, right_keycode) {
    _classCallCheck(this, Category);

    this.round_number = round_number;
    this.left_main_category = left_main_category;
    this.right_main_category = right_main_category;
    this.left_sub_category = left_sub_category;
    this.right_sub_category = right_sub_category;
    this.left_keycode = left_keycode;
    this.right_keycode = right_keycode;
};

var Item = function Item(iat_item, correct_side) {
    _classCallCheck(this, Item);

    this.iat_item = iat_item;
    this.correct_side = correct_side;
};

var Keypress = function Keypress(period, keycode, timestamp) {
    _classCallCheck(this, Keypress);

    this.period = period;
    this.keycode = keycode;
    this.timestamp = timestamp;
};

var Iat = function Iat(period, left_main_category, right_main_category, left_sub_category, right_sub_category, item, correct_side, timestamp, elapsed_time, pressed_key, pressed_side) {
    _classCallCheck(this, Iat);

    this.period = period;
    this.left_main_category = left_main_category;
    this.right_main_category = right_main_category;
    this.left_sub_category = left_sub_category;
    this.right_sub_category = right_sub_category;
    this.item = item;
    this.correct_side = correct_side;
    this.timestamp = timestamp;
    this.elapsed_time = elapsed_time;
    this.pressed_key = pressed_key;
    this.pressed_side = pressed_side;
};

var begin = function begin() {
    load_current_quiz();
    wait_for_answer();
};

var clear_screen = function clear_screen() {
    // clear screen
    hide_all_boxes();
    $("html").fadeOut(100);
};

var hide_all_boxes = function hide_all_boxes() {
    $('.next_block_box').hide();
    $('.wrong_key_box').css('opacity', '0');
    $('.wrong_answer_mark').hide();
};

var load_current_quiz = function load_current_quiz() {
    current_item = iat_items[current_period - 1];
    timer = new Timer();
    $('html').fadeIn(0);
    var is_main_or_sub = void 0;
    if (determine_item_in_main(current_item)) is_main_or_sub = "main";else is_main_or_sub = "sub";
    $('#keyword').html(current_item.toString()).removeClass("main sub").addClass(is_main_or_sub);

    //$('#progress').html(current_period.toString()+"/"+last_period.toString());
};

var determine_item_in_main = function determine_item_in_main(keyword) {
    return main_items.indexOf(keyword) !== -1;
};

var prepare_next_quiz = function prepare_next_quiz() {
    // prepare next quiz
    current_period++;
    begin();
};

var is_last_period = function is_last_period() {
    return current_period >= last_period;
};

var save_and_exit = function save_and_exit() {
    var category_table_JSON = JSON.stringify(category_table);
    var item_table_JSON = JSON.stringify(item_table);
    var keypress_table_JSON = JSON.stringify(keypress_table);
    var iat_table_JSON = JSON.stringify(iat_table);

    $('#category_table').val(category_table_JSON);
    $('#item_table').val(item_table_JSON);
    $('#keypress_table').val(keypress_table_JSON);
    $('#iat_table').val(iat_table_JSON);
    $('#form').submit();
};

var convert_to_csv = function convert_to_csv(table) {
    var Json2csvParser = require('json2csv').Parser;
    var parser = new Json2csvParser();
    var csv = parser.parse(table);
    // console.log(csv);
};

var wait_for_answer = function wait_for_answer() {
    // wait for keydown. 
};

var Timer = function () {
    // begin timer, end timer, and difference time.
    function Timer() {
        _classCallCheck(this, Timer);

        this.start_time = new Date().getTime();
    }

    _createClass(Timer, [{
        key: 'start',
        value: function start() {
            this.start_time = new Date().getTime();
        }
    }, {
        key: 'get_elapsed',
        value: function get_elapsed() {
            return new Date().getTime() - this.start_time;
        }
    }]);

    return Timer;
}();

;

var is_key_valid = function is_key_valid(keycode) {
    return keycode === left_keycode || keycode === right_keycode;
};

var mark_wrong = function mark_wrong() {
    $(".wrong_answer_mark").show();
};

var is_correct = function is_correct(pressed_side, correct_side) {
    return pressed_side === correct_side;
};

var which_side = function which_side(keycode) {
    if (keycode === left_keycode) return side['left'];else if (keycode === right_keycode) return side['right'];else return undefined;
};

var display_next_block_box = function display_next_block_box() {
    $(".next_block_box").show();
};

/** data stack strategy

- longstring csv 로 저장하는 것은 OECD와 같음
- 피리어드별 데이터가 입력되고 있는 것과 달리 vertical stack을 할까 함.
- period, key, timestamp의 방식.
- 일단 multi table. 디버깅을 위한 것이기도 함.
- table 1(category_table): 해당 블럭 기본 정보. - left_main_category, right_main_category, left_sub_category, right_sub_category
- table 2(item_table): 해당 블럭 문제 - iat_item, correct_side
- table 3(keypress_table): 키입력 timestamp - period, keycode, timestamp (무슨 키가 눌렸든)
- table 4(iat_table): 문제 (human readable) -
    period, left_category, right_category, item, correct_side (LR), timestamp, elapsed_time
    이건 L or R 키가 눌린 거만

 */
// table declaration

var category_table = [];
var item_table = [];
var keypress_table = [];
var iat_table = [];

// global variables initialization

// console.log("IAT.html script begin!");

category_table.push(new Category(round_number, category.main.left, category.main.right, category.sub.left, category.sub.right, left_keycode, right_keycode));
item_table.push(new Item(iat_items, correct_sides));

// console.log(category);

var current_period = 1;
var last_period = iat_items.length;
var timer = void 0;

$(document).ready(function () {
    begin();
});

$(document).keydown(function (event) {
    if (current_period > last_period) {
        display_next_block_box();
        if (event.which === META_KEYCODE) {
            // console.log("meta key pressed!");
            save_and_exit();
        }
        return;
    }
    keypress_table.push(new Keypress(current_period, event.which, new Date().getTime()));
    var pressed_side = null;
    if (is_key_valid(event.which)) {
        pressed_side = which_side(event.which);
        iat_table.push(new Iat(current_period, category.main.left, category.main.right, category.sub.left, category.sub.right, iat_items[current_period - 1], correct_sides[current_period - 1], new Date().getTime(), timer.get_elapsed(), event.which, pressed_side));
        if (!is_correct(pressed_side, correct_sides[current_period - 1])) {
            mark_wrong();
            return;
        }
        if (is_last_period()) {
            current_period++;
            hide_all_boxes();
            display_next_block_box();
            return;
        } else {
            clear_screen();
            prepare_next_quiz();
        }
    } else {
        // display warning (올바른 키를 입력해야 합니다. wrong key에 대한 data stack)
        $('.wrong_key_box').css('opacity', '1');
    }
});