from flappening.entities import Particle


def test_particle():

    position1: list = [150, 250]
    size1: list = [25, 50]

    position2: list = [-25, -25]
    size2: list = [10, 10]

    position3: list = [150, 225]
    size3: list = [50, 50]

    # create particle's
    particle1 = Particle(position1, size1)
    particle2 = Particle(position2, size2)
    particle3 = Particle(position3, size3)

    # check if positions are saved:
    assert particle1.x == position1[0]
    assert particle1.y == position1[1]

    # check if size is saved:
    assert list(particle1.size) == [25, 50]

    # check if is inBound and visible
    assert particle1.inBound()
    assert particle1.visible()

    # check if is not inBound and not visible
    assert not particle2.inBound()
    assert not particle2.visible()

    # check if collision
    assert not particle1.collision(particle2)
    assert particle1.collision(particle3)
