"""
Cartesian Product Functorial Construction

AUTHORS:

 - Nicolas M. Thiery (2008-2010): initial revision and refactorization
"""
#*****************************************************************************
#  Copyright (C) 2010 Nicolas M. Thiery <nthiery at users.sf.net>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.categories.covariant_functorial_construction import CovariantFunctorialConstruction, CovariantConstructionCategory

class CartesianProductFunctor(CovariantFunctorialConstruction):
    """
    A singleton class for the Cartesian product functor.

    EXAMPLES::

        sage: cartesian_product
        The cartesian_product functorial construction

    ``cartesian_product`` takes a finite collection of sets, and
    constructs the Cartesian product of those sets::

        sage: A = FiniteEnumeratedSet(['a','b','c'])
        sage: B = FiniteEnumeratedSet([1,2])
        sage: C = cartesian_product([A, B]); C
        The cartesian product of ({'a', 'b', 'c'}, {1, 2})
        sage: C.an_element()
        ('a', 1)
        sage: C.list()         # todo: not implemented
        [['a', 1], ['a', 2], ['b', 1], ['b', 2], ['c', 1], ['c', 2]]

    If those sets are endowed with more structure, say they are
    monoids (hence in the category `Monoids()`), then the result is
    automatically endowed with its natural monoid structure::

         sage: M = Monoids().example()
         sage: M
         An example of a monoid: the free monoid generated by ('a', 'b', 'c', 'd')
         sage: M.rename('M')
         sage: C = cartesian_product([M, ZZ, QQ])
         sage: C
         The cartesian product of (M, Integer Ring, Rational Field)
         sage: C.an_element()
         ('abcd', 1, 1/2)
         sage: C.an_element()^2
         ('abcdabcd', 1, 1/4)
         sage: C.category()
         Category of Cartesian products of monoids

         sage: Monoids().CartesianProducts()
         Category of Cartesian products of monoids

    The Cartesian product functor is covariant: if ``A`` is a
    subcategory of ``B``, then ``A.CartesianProducts()`` is a
    subcategory of ``B.CartesianProducts()`` (see also
    :class:`~sage.categories.covariant_functorial_construction.CovariantFunctorialConstruction`)::

         sage: C.categories()
         [Category of Cartesian products of monoids,
          Category of monoids,
          Category of Cartesian products of semigroups,
          Category of semigroups,
          Category of Cartesian products of magmas,
          Category of unital magmas,
          Category of magmas,
          Category of Cartesian products of sets,
          Category of sets,
          Category of sets with partial maps,
          Category of objects]

    Hence, the role of ``Monoids().CartesianProducts()`` is solely to
    provide mathematical information and algorithms which are relevant
    to Cartesian product of monoids. For example, it specifies that
    the result is again a monoid, and that its multiplicative unit is
    the cartesian product of the units of the underlying sets::

        sage: C.one()
        ('', 1, 1)

    Those are implemented in the nested class
    :class:`Monoids.CartesianProducts
    <sage.categories.monoids.Monoids.CartesianProducts>` of
    ``Monoids(QQ)``. This nested class is itself a subclass of
    :class:`CartesianProductsCategory`.

    """
    _functor_name = "cartesian_product"
    _functor_category = "CartesianProducts"
    symbol = " (+) "

cartesian_product = CartesianProductFunctor()
"""
The cartesian product functorial construction.

See :class:`CartesianProductFunctor` for more information.

EXAMPLES::

    sage: cartesian_product
    The cartesian_product functorial construction
"""

class CartesianProductsCategory(CovariantConstructionCategory):
    """
    An abstract base class for all ``CartesianProducts`` categories.

    TESTS::

        sage: C = Sets().CartesianProducts()
        sage: C
        Category of Cartesian products of sets
        sage: C.base_category()
        Category of sets
        sage: latex(C)
        \mathbf{CartesianProducts}(\mathbf{Sets})
    """

    _functor_category = "CartesianProducts"

    def _repr_object_names(self):
        """
        EXAMPLES::

            sage: ModulesWithBasis(QQ).CartesianProducts() # indirect doctest
            Category of Cartesian products of modules with basis over Rational Field

        """
        # This method is only required for the capital `C`
        return "Cartesian products of %s"%(self.base_category()._repr_object_names())

    def CartesianProducts(self):
        """
        Return the category of (finite) Cartesian products of objects
        of ``self``.

        By associativity of Cartesian products, this is ``self`` (a Cartesian
        product of Cartesian products of `A`'s is a Cartesian product of
        `A`'s).

        EXAMPLES::

            sage: ModulesWithBasis(QQ).CartesianProducts().CartesianProducts()
            Category of Cartesian products of modules with basis over Rational Field
        """
        return self

    def base_ring(self):
        """
        The base ring of a cartesian product is the base ring of the underlying category.

        EXAMPLES::

            sage: Algebras(ZZ).CartesianProducts().base_ring()
            Integer Ring
        """
        return self.base_category().base_ring()
