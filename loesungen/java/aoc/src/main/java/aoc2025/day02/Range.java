package aoc2025.day02;

public class Range {
    private long lowerBound;
    private long upperBound;

    public Range(long lowerBound, long upperBound) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }

    public long getLowerBound() {
        return lowerBound;
    }

    public void setLowerBound(long lowerBound) {
        this.lowerBound = lowerBound;
    }

    public long getUpperBound() {
        return upperBound;
    }

    public void setUpperBound(long upperBound) {
        this.upperBound = upperBound;
    }

    @Override
    public String toString() {
        return "Range{" + "lowerBound=" + lowerBound + ", upperBound=" + upperBound + '}';
    }
}
