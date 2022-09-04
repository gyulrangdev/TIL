function solution(absolutes, signs) {
  return absolutes
    .map((elem, idx) => (signs[idx] ? elem : elem * -1))
    .reduce((partialSum, a) => partialSum + a, 0);
}
