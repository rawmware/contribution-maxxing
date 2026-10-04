// Demonstrate trait objects and generic static dispatch
pub trait Measure { fn area(&self) -> f64; }
pub struct Rectangle { width: f64, height: f64 }
impl Rectangle {
    /// Only finite nonnegative dimensions and representable areas are accepted.
    pub fn new(width: f64, height: f64) -> Option<Self> {
        if !width.is_finite() || !height.is_finite() || width < 0.0 || height < 0.0
            || !(width*height).is_finite() { return None; }
        Some(Self { width,height })
    }
}
impl Measure for Rectangle { fn area(&self) -> f64 { self.width*self.height } }
pub fn static_area<T: Measure>(shape: &T) -> f64 { shape.area() }
/// Dynamic dispatch; the sum can overflow even if individual areas are finite.
pub fn total_area(shapes: &[&dyn Measure]) -> Option<f64> {
    shapes.iter().try_fold(0.0, |sum,shape| {
        let next = sum+shape.area(); next.is_finite().then_some(next)
    })
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn dispatch() {
        let a = Rectangle::new(2.0,3.0).unwrap(); let b = Rectangle::new(4.0,5.0).unwrap();
        assert_eq!(static_area(&a),6.0); assert_eq!(total_area(&[&a,&b]),Some(26.0));
    }
    #[test] fn invalid_numbers() {
        assert!(Rectangle::new(f64::NAN,1.0).is_none());
        assert!(Rectangle::new(-1.0,1.0).is_none());
        assert!(Rectangle::new(f64::MAX,2.0).is_none());
    }
}
