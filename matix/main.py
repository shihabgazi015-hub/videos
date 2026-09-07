from manim import *

class MatrixRank(Scene):
    def construct(self):

       
        CYAN = "#00E5FF"
        MAGENTA = "#FF007F"
        RED_ACCENT = "#EF4444"
        GOLD = "#FACC15"
      
        matrix_data = [
            ["1", "0", "1", "1", "2"],
            ["0", "1", "1", "3", "0"],
            ["1", "1", "2", "4", "2"],
            ["2", "1", "3", "5", "4"]
        ]
        
        matrix = Matrix(matrix_data)
        matrix.get_brackets().set_color(CYAN)
        matrix.set_color(WHITE)
        
      
        col_labels = VGroup(*[MathTex(f"a_{i+1}").next_to(matrix.get_columns()[i], UP) for i in range(5)])
        
      
        counter_text = Text("20 Numbers", font_size=36, color=WHITE).to_edge(UP)
        
        self.play(FadeIn(matrix), FadeIn(col_labels))
        self.play(Write(counter_text))
        self.wait(1)

      
        rect_a1 = SurroundingRectangle(matrix.get_columns()[0], color=GREEN)
        rect_a2 = SurroundingRectangle(matrix.get_columns()[1], color=GREEN)
        
        check_a1 = MathTex(r"\checkmark", color=GREEN).next_to(matrix.get_columns()[0], DOWN)
        check_a2 = MathTex(r"\checkmark", color=GREEN).next_to(matrix.get_columns()[1], DOWN)
        
        self.play(Create(rect_a1), Create(rect_a2))
        self.play(Write(check_a1), Write(check_a2))
        
        rect_a3 = SurroundingRectangle(matrix.get_columns()[2], color=YELLOW)
        cross_a3 = MathTex(r"\times", color=RED).next_to(matrix.get_columns()[2], DOWN)
        eq_a3 = MathTex("a_3 = a_1 + a_2").to_edge(DOWN)
        
        self.play(Create(rect_a3), Write(cross_a3))
        self.play(Write(eq_a3))
        self.wait(1)
        
        rect_a4 = SurroundingRectangle(matrix.get_columns()[3], color=YELLOW)
        cross_a4 = MathTex(r"\times", color=RED).next_to(matrix.get_columns()[3], DOWN)
        eq_a4 = MathTex("a_4 = a_1 + 3a_2").to_edge(DOWN)
        
        self.play(Transform(rect_a3, rect_a4), Write(cross_a4), Transform(eq_a3, eq_a4))
        self.wait(1)
        
        rect_a5 = SurroundingRectangle(matrix.get_columns()[4], color=YELLOW)
        cross_a5 = MathTex(r"\times", color=RED).next_to(matrix.get_columns()[4], DOWN)
        eq_a5 = MathTex("a_5 = 2a_1").to_edge(DOWN)
        
        self.play(Transform(rect_a3, rect_a5), Write(cross_a5), Transform(eq_a3, eq_a5))
        self.wait(1)

   
        self.play(FadeOut(rect_a1, rect_a2, rect_a3, check_a1, check_a2, cross_a3, cross_a4, cross_a5, eq_a3, counter_text))
        
        rank_text = MathTex(r"\text{Rank} = 2", color=CYAN).to_edge(UP)
        self.play(Write(rank_text))
     
        ingredients_data = [["1", "0"], ["0", "1"], ["1", "1"], ["2", "1"]]
        recipes_data = [["1", "0", "1", "1", "2"], ["0", "1", "1", "3", "0"]]
        
        mat_ingredients = Matrix(ingredients_data).set_color(GREEN)
        mat_recipes = Matrix(recipes_data).set_color(ORANGE)
        
        equals = MathTex("=").scale(1.5)
        factorization_group = VGroup(mat_ingredients, mat_recipes).arrange(RIGHT)
     
        self.play(
            FadeOut(col_labels),
            ReplacementTransform(matrix, mat_ingredients),
            FadeIn(factorization_group[0]), 
            FadeIn(mat_recipes)             
        )

        self.wait(2)

        row_highlight = SurroundingRectangle(mat_ingredients.get_rows()[0], color=YELLOW)
        col_highlight = SurroundingRectangle(mat_recipes.get_columns()[0], color=YELLOW)
        
        self.play(Create(row_highlight), Create(col_highlight))
        for i in range(1, 4):
            self.play(
                row_highlight.animate.move_to(mat_ingredients.get_rows()[i]),
                col_highlight.animate.move_to(mat_recipes.get_columns()[i % 2]),
                run_time=0.5
            )
        self.play(FadeOut(row_highlight, col_highlight))
        self.wait(1)
        
        self.play(FadeOut(matrix, mat_ingredients, mat_recipes, rank_text))
        
        big_matrix_box = Rectangle(width=4, height=4, color=WHITE)
        big_text = Text("1000 x 1000", font_size=32).move_to(big_matrix_box)
        num_counter = ValueTracker(1000000)
        
        counter_display = always_redraw(
            lambda: Text(f"{int(num_counter.get_value()):,} Numbers", color=WHITE).to_edge(UP)
        )
        
        self.play(Create(big_matrix_box), Write(big_text), FadeIn(counter_display))
        self.wait(1)
       
        thin_block = Rectangle(width=1, height=4, color=GREEN).shift(LEFT * 2)
        flat_block = Rectangle(width=4, height=1, color=ORANGE).shift(RIGHT * 2)
        
        self.play(
            Transform(big_matrix_box, VGroup(thin_block, flat_block)),
            FadeOut(big_text),
            num_counter.animate.set_value(20000),
            run_time=2
        )
        
        reduction_text = Text("98% Reduction", color=CYAN, font_size=40).next_to(counter_display, DOWN)
        self.play(Write(reduction_text))
        self.wait(1)
        
        apps_text = Text("Image Compression • PCA • SVD", font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(apps_text))
        self.wait(3)
