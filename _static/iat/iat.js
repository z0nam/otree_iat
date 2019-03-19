console.log("hello, iat!");

class Category {
    constructor(round_number, left_main_category, right_main_category,
                left_sub_category, right_sub_category, left_keycode, right_keycode) {
                    this.round_number = round_number;
                    this.left_main_category = left_main_category;
                    this.right_main_category = right_main_category;
                    this.left_sub_category = left_sub_category;
                    this.right_sub_category = right_sub_category;
                    this.left_keycode = left_keycode;
                    this.right_keycode = right_keycode;
                }
}

class Item {
    constructor(iat_item, correct_side) {
        this.iat_item = iat_item;
        this.correct_side = correct_side;
    }
}

class Keypress {
    constructor(period, keycode, timestamp) {
        this.period = period;
        this.keycode = keycode;
        this.timestamp = timestamp;
    }
}

class Iat {
    constructor(period, left_main_category, right_main_category,
                left_sub_category, right_sub_category, item,
                correct_side, timestamp, elapsed_time, pressed_key, pressed_side) {
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
      }
}

const begin = () => {
    console.log("begin() begin!");
    load_current_quiz();
    wait_for_answer();
};

const clear_screen = () => {
    // clear screen
    hide_all_boxes();
    $("html").fadeOut(100);
};

const hide_all_boxes = () => {
    $('.next_block_box').hide();
    $('.wrong_key_box').css('opacity','0');
    $('.wrong_answer_mark').hide();
}

const load_current_quiz = () => {
    current_item = iat_items[current_period-1];
    timer = new Timer();
    $('html').fadeIn(0);
    $('#keyword').html(current_item.toString());
    //$('#progress').html(current_period.toString()+"/"+last_period.toString());
};

const prepare_next_quiz = () => {
    // prepare next quiz
    current_period++;
    begin();
};

const is_last_period = () => {
    return (current_period >= last_period)
};

const save_and_exit_old = () => {
    // save current response and pass over csv format (like OECD iat test)
    const category_table_csv = convert_to_csv(category_table);
    const item_table_csv = convert_to_csv(item_table);
    const keypress_table_csv = convert_to_csv(keypress_table);
    const iat_table_csv = convert_to_csv(iat_table);

    $('#category_table').val(category_table_csv);
    $('#item_table').val(item_table_csv);
    $('#keypress_table').val(keypress_table_csv);
    $('#iat_table').val(iat_table_csv);
    $('#form').submit();
};

const save_and_exit = () => {
    const category_table_JSON = JSON.stringify(category_table);
    const item_table_JSON = JSON.stringify(item_table);
    const keypress_table_JSON = JSON.stringify(keypress_table);
    const iat_table_JSON = JSON.stringify(iat_table);

    $('#category_table').val(category_table_JSON);
    $('#item_table').val(item_table_JSON);
    $('#keypress_table').val(keypress_table_JSON);
    $('#iat_table').val(iat_table_JSON);
    $('#form').submit();
};

const convert_to_csv = (table) => {
    const Json2csvParser = require('json2csv').Parser;
    const parser = new Json2csvParser();
    const csv = parser.parse(table);
    console.log(csv);
};

const wait_for_answer = () => {
    // wait for keydown. 
};

class Timer {
    // begin timer, end timer, and difference time.
    constructor() {
        this.start_time = new Date().getTime();
    }

    start(){
        this.start_time = new Date().getTime();
    };

    get_elapsed() {
        return new Date().getTime() - this.start_time;
    };


};

const is_key_valid = (keycode) => {
    return keycode === left_keycode || keycode === right_keycode;
};

const mark_wrong = () => {
        $(".wrong_answer_mark").show();
};

const is_correct = (pressed_side, correct_side) => {
    return (pressed_side === correct_side);
};

const which_side = (keycode) => {
    if (keycode === left_keycode) return side['left'];
    else if (keycode === right_keycode) return side['right'];
    else return undefined;
};

const display_next_block_box = () => {
    $(".next_block_box").show();
}