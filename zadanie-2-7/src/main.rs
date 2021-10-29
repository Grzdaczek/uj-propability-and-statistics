fn no_club_in_3() -> bool {
    let clubs = 13.0;
    let mut all = 52.0;

    for _ in 0..3 {
        if rand::random::<f32>() < clubs / all {
            return true;
        }
        else {
            all -= 1.0;
        }
    }

    return false;
}
fn main() {
    let mut a = 0;
    let mut b = 0;
    let mut err = 1.0;
    let mut p_m = 0.0;
    let p_t = 0.413529412;

    while err > 0.001 {
        if !no_club_in_3() { a += 1 }
        b += 1;
        p_m = a as f32 / b as f32;
        err = (p_t - p_m).abs() / p_m;
    }

    println!("theoretical propability: {}", &p_t);
    println!("mesured propability: {}", &p_m);
    println!("tries: {}", &b);
    println!("error: {}", &err);
    // println!("{}", a as f32 / b as f32);
}
