
#include <vector>
#include <string>

namespace graph_tradeoff
{
    class NeighborView
    {
    public:
        using container_type = std::vector<int>;
        using const_iterator = container_type::const_iterator;
        using const_reverse_iterator = container_type::const_reverse_iterator;
        NeighborView() = default;
        explicit NeighborView(const container_type &neighbors) : borrowed_(&neighbors) {}

        explicit NeighborView(container_type &&owned_neighbors) : owned_(std::move(owned_neighbors)), borrowed_(&owned_) {}

        const_iterator begin() const { return borrowed_->begin(); }
        const_iterator end() const { return borrowed_->end(); }

        bool empty() const { return borrowed_->empty(); }
        std::size_t size() const { return borrowed_->size(); }
        int operator[](std::size_t index) const
        {
            return (*borrowed_)[index];
        }
        const_reverse_iterator rbegin() const
        {
            return borrowed_->rbegin();
        }

        const_reverse_iterator rend() const
        {
            return borrowed_->rend();
        }

    private:
        container_type owned_{};
        const container_type *borrowed_ = &owned_;
    };

} // namespace graph_tradeoff
