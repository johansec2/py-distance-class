from typing import Union


class Distance:
    """A class to represent a distance in kilometers."""

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def _get_km(self, other: Union["Distance", int, float]) -> Union[int, float]:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(
                f"Unsupported operand type: {type(other)}"
            )

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        other_km = self._get_km(other)
        return Distance(self.km + other_km)

    def __radd__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            f"Unsupported operand type: {type(other)}"
        )

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        other_km = self._get_km(other)
        self.km += other_km
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"Unsupported operand type: {type(other)}"
        )

    def __rmul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"Unsupported operand type: {type(other)}"
        )

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))
        raise TypeError(
            f"Unsupported operand type: {type(other)}"
        )

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (Distance, int, float)):
            return self.km == self._get_km(other)
        return NotImplemented

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        return self.km >= self._get_km(other)
