r"""
Complete Discrete Valuation Rings (CDVR) and Fields (CDVF)
"""
from __future__ import absolute_import
#**************************************************************************
#  Copyright (C) 2013 Xavier Caruso <xavier.caruso@normalesup.org>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#**************************************************************************


from sage.misc.abstract_method import abstract_method

from sage.categories.category_singleton import Category_singleton
from .discrete_valuation import DiscreteValuationRings, DiscreteValuationFields
#from sage.misc.cachefunc import cached_method


class CompleteDiscreteValuationRings(Category_singleton):
    """
    The category of complete discrete valuation rings

    EXAMPLES::

        sage: Zp(7) in CompleteDiscreteValuationRings()
        True
        sage: QQ in CompleteDiscreteValuationRings()
        False
        sage: QQ[['u']] in CompleteDiscreteValuationRings()
        True
        sage: Qp(7) in CompleteDiscreteValuationRings()
        False
        sage: TestSuite(CompleteDiscreteValuationRings()).run()
    """
    def super_categories(self):
        """
        EXAMPLES::

            sage: CompleteDiscreteValuationRings().super_categories()
            [Category of discrete valuation rings]
        """
        return [DiscreteValuationRings()]

    class ElementMethods:
        @abstract_method
        def precision_absolute(self):
            """
            Return the absolute precision of this element.

            EXAMPLES::

                sage: R = Zp(7)
                sage: x = R(7); x
                7 + O(7^21)
                sage: x.precision_absolute()
                21
            """

        @abstract_method
        def precision_relative(self):
            """
            Return the relative precision of this element.

            EXAMPLES::

                sage: R = Zp(7)
                sage: x = R(7); x
                7 + O(7^21)
                sage: x.precision_relative()
                20
            """

        @abstract_method
        def lift_to_maximal_precision(self):
            """
            Lift this element to the maximal precision
            allowed by the parent.

            EXAMPLES::

                sage: R = Zp(7,prec=20)
                sage: x = R(7,5); x
                7 + O(7^5)
                sage: x.lift_to_maximal_precision()
                7 + O(7^21)
            """

        @abstract_method
        def lift_to_precision(self, absprec=None):
            """
            Return another element of the same parent with absolute precision
            at least ``absprec``, congruent to this element modulo the
            precision of this element.

            INPUT:

            - ``absprec`` -- an integer or ``None`` (default: ``None``), the
              absolute precision of the result. If ``None``, lifts to the maximum
              precision allowed.

            .. NOTE::

                If setting ``absprec`` that high would violate the precision cap,
                raises a precision error.  Note that the new digits will not
                necessarily be zero.

            EXAMPLES::

                sage: R = ZpCA(17)
                sage: R(-1,2).lift_to_precision(10)
                16 + 16*17 + O(17^10)
                sage: R(1,15).lift_to_precision(10)
                1 + O(17^15)
                sage: R(1,15).lift_to_precision(30)
                Traceback (most recent call last):
                ...
                PrecisionError: Precision higher than allowed by the precision cap.
                sage: R(-1,2).lift_to_precision().precision_absolute() == R.precision_cap()
                True

                sage: R = Zp(5); c = R(17,3); c.lift_to_precision(8)
                2 + 3*5 + O(5^8)
                sage: c.lift_to_precision().precision_relative() == R.precision_cap()
                True

            """

class CompleteDiscreteValuationFields(Category_singleton):
    """
    The category of complete discrete valuation fields

    EXAMPLES::

        sage: Zp(7) in CompleteDiscreteValuationFields()
        False
        sage: QQ in CompleteDiscreteValuationFields()
        False
        sage: LaurentSeriesRing(QQ,'u') in CompleteDiscreteValuationFields()
        True
        sage: Qp(7) in CompleteDiscreteValuationFields()
        True
        sage: TestSuite(CompleteDiscreteValuationFields()).run()
    """

    def super_categories(self):
        """
        EXAMPLES::

            sage: CompleteDiscreteValuationFields().super_categories()
            [Category of discrete valuation fields]
        """
        return [DiscreteValuationFields()]

    class ParentMethods:
        @abstract_method
        def tracks_precision(self):
            r"""
            Return whether elements in this parent track precision.

            EXAMPLES::

                sage: R = Zp(5)
                sage: R.tracks_precision()
                True

                sage: R = ZpFP(5)
                sage: R.tracks_precision()
                False
            """

    class ElementMethods:
        @abstract_method
        def precision_absolute(self):
            """
            Return the absolute precision of this element.

            EXAMPLES::

                sage: K = Qp(7)
                sage: x = K(7); x
                7 + O(7^21)
                sage: x.precision_absolute()
                21
            """

        @abstract_method
        def precision_relative(self):
            """
            Return the relative precision of this element.

            EXAMPLES::

                sage: K = Qp(7)
                sage: x = K(7); x
                7 + O(7^21)
                sage: x.precision_relative()
                20
            """
